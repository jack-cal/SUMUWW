"""Select native-size taskbar icons without changing the official artwork."""
import ctypes
from ctypes import wintypes
import sys


# A window class can outlive any one Tk window. Keep one pair per artwork
# and Windows icon size for the lifetime of this process.
_icon_pairs = {}


def install_taskbar_icon(root, path):
    if sys.platform != 'win32':
        return
    root._sumuww_native_icon_path = path
    if not getattr(root, '_sumuww_native_icon_map_bound', False):
        # A withdrawn Tk window may not yet have its outer Windows wrapper.
        # Install on that wrapper once it is mapped; the identity check below
        # makes subsequent Map events reuse the existing handles.
        def mapped(event):
            if event.widget is root:
                install_taskbar_icon(root, root._sumuww_native_icon_path)
        root.bind('<Map>', mapped, add='+')
        root._sumuww_native_icon_map_bound = True
    user32 = ctypes.WinDLL('user32', use_last_error=True)
    user32.GetAncestor.argtypes = [wintypes.HWND, wintypes.UINT]
    user32.GetAncestor.restype = wintypes.HWND
    user32.LoadImageW.argtypes = [wintypes.HINSTANCE, wintypes.LPCWSTR, wintypes.UINT,
                                ctypes.c_int, ctypes.c_int, wintypes.UINT]
    user32.LoadImageW.restype = wintypes.HANDLE
    user32.SendMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
    user32.SendMessageW.restype = wintypes.LPARAM
    user32.DestroyIcon.argtypes = [wintypes.HANDLE]
    hwnd = user32.GetAncestor(root.winfo_id(), 2) or root.winfo_id()
    user32.GetClassNameW.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
    class_name = ctypes.create_unicode_buffer(64)
    user32.GetClassNameW(hwnd, class_name, len(class_name))
    dpi = 96
    if hasattr(user32, 'GetDpiForWindow'):
        user32.GetDpiForWindow.argtypes = [wintypes.HWND]
        user32.GetDpiForWindow.restype = wintypes.UINT
        dpi = user32.GetDpiForWindow(hwnd) or 96
    # DPI-unaware Tk windows report 96 even on a scaled monitor. Read the
    # monitor's physical scale without changing the wallet UI's DPI behaviour.
    try:
        user32.MonitorFromWindow.argtypes = [wintypes.HWND, wintypes.DWORD]
        user32.MonitorFromWindow.restype = wintypes.HANDLE
        shcore = ctypes.WinDLL('shcore')
        shcore.GetScaleFactorForMonitor.argtypes = [wintypes.HANDLE, ctypes.POINTER(ctypes.c_int)]
        scale = ctypes.c_int()
        if shcore.GetScaleFactorForMonitor(user32.MonitorFromWindow(hwnd, 2), ctypes.byref(scale)) == 0:
            dpi = max(dpi, round(96 * scale.value / 100))
    except (OSError, AttributeError):
        pass
    sizes = []
    for metric in (11, 49):  # SM_CXICON / SM_CXSMICON.
        if hasattr(user32, 'GetSystemMetricsForDpi'):
            user32.GetSystemMetricsForDpi.argtypes = [ctypes.c_int, wintypes.UINT]
            size = user32.GetSystemMetricsForDpi(metric, dpi)
        else:
            size = user32.GetSystemMetrics(metric)
        sizes.append(size)
    key = (str(path.resolve()), tuple(sizes))
    handles = _icon_pairs.get(key)
    if handles is None:
        handles = [user32.LoadImageW(None, str(path), 1, size, size, 0x10) for size in sizes]
        if not all(handles):
            for handle in handles:
                if handle:
                    user32.DestroyIcon(handle)
            return
        _icon_pairs[key] = handles

    # Explorer can use the class icons for the taskbar and the window icons
    # for its preview. Assign both, including the small class icon.
    set_class_icon = (user32.SetClassLongPtrW if ctypes.sizeof(ctypes.c_void_p) == 8
                      else user32.SetClassLongW)
    set_class_icon.argtypes = [wintypes.HWND, ctypes.c_int, wintypes.HANDLE]
    set_class_icon.restype = ctypes.c_size_t
    if class_name.value == 'TkTopLevel':
        for index, handle in zip((-14, -34), handles):  # GCLP_HICON, GCLP_HICONSM.
            ctypes.set_last_error(0)
            if not set_class_icon(hwnd, index, handle) and ctypes.get_last_error():
                raise ctypes.WinError(ctypes.get_last_error())
    for slot, handle in zip((1, 0), handles):
        user32.SendMessageW(hwnd, 0x80, slot, handle)  # WM_SETICON.
    root._sumuww_native_icon_identity = (key[0], hwnd, key[1])
    root._sumuww_taskbar_icon_sizes = tuple(sizes)
    if class_name.value == 'TkTopLevel' and getattr(root, '_sumuww_full_node_taskbar', False):
        from .taskbar_identity import set_full_node_identity
        set_full_node_identity(root, hwnd, path)
