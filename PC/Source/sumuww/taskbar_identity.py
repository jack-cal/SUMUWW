"""Windows Shell metadata for the full node's taskbar button."""
import ctypes
from ctypes import wintypes
from pathlib import Path
import subprocess
import sys
from uuid import UUID


class PropertyKey(ctypes.Structure):
    _fields_ = [('fmtid', ctypes.c_uint32 * 4), ('pid', wintypes.DWORD)]


class PropVariant(ctypes.Structure):
    # PROPVARIANT's union holds up to two pointer-sized words.
    _fields_ = [('vt', ctypes.c_ushort), ('reserved', ctypes.c_ushort * 3),
                ('data', ctypes.c_void_p * 2)]


def _guid(value):
    return (ctypes.c_uint32 * 4).from_buffer_copy(UUID(value).bytes_le)


_APP = _guid('9f4c2855-9f79-4b39-a8d0-e1d42de1d5f3')
_STORE = _guid('886d8eeb-8cf2-4446-8d02-cdba1dbdcf99')


def _set_properties(hwnd, values):
    shell = ctypes.OleDLL('shell32').SHGetPropertyStoreForWindow
    shell.argtypes = [wintypes.HWND, ctypes.POINTER(type(_STORE)),
                      ctypes.POINTER(ctypes.c_void_p)]
    store = ctypes.c_void_p()
    shell(hwnd, ctypes.byref(_STORE), ctypes.byref(store))
    table = ctypes.cast(store, ctypes.POINTER(ctypes.POINTER(ctypes.c_void_p))).contents
    release = ctypes.WINFUNCTYPE(wintypes.ULONG, ctypes.c_void_p)(table[2])
    set_value = ctypes.WINFUNCTYPE(ctypes.HRESULT, ctypes.c_void_p, ctypes.POINTER(PropertyKey),
                                   ctypes.POINTER(PropVariant))(table[6])
    try:
        for pid, value in values:
            prop = PropVariant()
            if value is not None:
                string = ctypes.create_unicode_buffer(value)
                prop.vt = 31  # VT_LPWSTR; SetValue copies the string.
                prop.data[0] = ctypes.addressof(string)
            set_value(store, ctypes.byref(PropertyKey(_APP, pid)), ctypes.byref(prop))
    finally:
        release(store)


def set_full_node_identity(root, hwnd, path):
    identity = hwnd, str(path.resolve())
    previous = getattr(root, '_sumuww_shell_identity', None)
    if previous == identity:
        return
    # Set the group's artwork and relaunch metadata before the explicit ID.
    # Explorer caches artwork by group even after its window properties change.
    # Languages sharing the default mark also share the original group.
    group = 'SUMUWW.Desktop.FullNode'
    if path.stem in ('ko', 'ar'):
        group += '.' + path.stem.upper()
    exe = Path(sys.executable)
    command = subprocess.list2cmdline([str(exe), *sys.argv[1:]])
    values = [(2, command), (4, 'SUMUWW'), (3, identity[1] + ',0'),
              (5, group)]
    try:
        _set_properties(hwnd, values)
    except OSError as error:
        # Explorer limits the relaunch command independently of Win32's command
        # line limit. A long data-directory argument must not hide the artwork.
        if error.winerror != -2147024774:  # HRESULT_FROM_WIN32(ERROR_INSUFFICIENT_BUFFER)
            raise
        _set_properties(hwnd, [(2, None), *values[1:]])
    root._sumuww_shell_identity = identity
    if not getattr(root, '_sumuww_shell_cleanup', False):
        def clear(event):
            if event.widget is root:
                try:
                    _set_properties(root._sumuww_shell_identity[0],
                                    [(5, None), (3, None), (4, None), (2, None)])
                except OSError:
                    pass  # The native wrapper may already have been destroyed.
        root.bind('<Destroy>', clear, add='+')
        root._sumuww_shell_cleanup = True
