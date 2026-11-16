import ctypes
from ctypes import wintypes
import sys
import tkinter as tk
import unittest
from unittest.mock import patch

from sumuww.brand import apply_window_icon
from sumuww import taskbar_identity


@unittest.skipUnless(sys.platform == 'win32', 'Requires a native Tk window on Windows')
class WindowsTaskbarTests(unittest.TestCase):
    def test_long_launch_arguments_do_not_suppress_the_icon(self):
        root = tk.Tk()
        self.addCleanup(root.destroy)
        root._sumuww_full_node_taskbar = True
        root.update()
        with patch.object(sys, 'argv', ['SUMUWW.exe', '--directory', 'd' * 300]):
            apply_window_icon(root, 'ar')
        self.assertEqual(root._sumuww_shell_identity[1],
                         root._sumuww_native_icon_identity[0])

    def test_live_language_switch_sets_the_group_for_the_actual_artwork(self):
        root = tk.Tk()
        self.addCleanup(root.destroy)
        root._sumuww_full_node_taskbar = True
        root.update()
        with patch.object(taskbar_identity, '_set_properties',
                          wraps=taskbar_identity._set_properties) as write:
            for language, suffix in [('en', ''), ('ko', '.KO'), ('ar', '.AR'),
                                     ('ko', '.KO'), ('fr', '')]:
                write.reset_mock()
                apply_window_icon(root, language)
                hwnd, values = write.call_args.args
                self.assertEqual(hwnd, root._sumuww_native_icon_identity[1])
                properties = dict(values)
                self.assertEqual(properties[5], 'SUMUWW.Desktop.FullNode' + suffix)
                icon = language if suffix else 'sumuww'
                self.assertTrue(properties[3].endswith(icon + '.ico,0'))
            write.reset_mock()
            apply_window_icon(root, 'de')  # Same artwork as French.
            write.assert_not_called()

    def test_class_and_window_icons_follow_the_language_and_survive_remapping(self):
        root = tk.Tk()
        self.addCleanup(root.destroy)
        root._sumuww_full_node_taskbar = True
        root.withdraw()
        root.attributes('-alpha', 0)
        apply_window_icon(root, 'en')
        root.deiconify()
        root.update()

        user32 = ctypes.WinDLL('user32')
        read_class = (user32.GetClassLongPtrW if ctypes.sizeof(ctypes.c_void_p) == 8
                      else user32.GetClassLongW)
        read_class.argtypes = [wintypes.HWND, ctypes.c_int]
        read_class.restype = ctypes.c_size_t
        get_icon = user32.SendMessageW
        get_icon.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
        get_icon.restype = wintypes.LPARAM
        seen = {}
        for language in ('en', 'ko', 'ar', 'en', 'ko'):
            apply_window_icon(root, language)
            root.withdraw()
            root.deiconify()
            root.update()
            hwnd = root._sumuww_native_icon_identity[1]
            window = tuple(get_icon(hwnd, 0x7f, slot, 0) for slot in (1, 0))
            self.assertTrue(all(window))
            self.assertEqual(tuple(read_class(hwnd, index) for index in (-14, -34)), window)
            self.assertEqual(root._sumuww_shell_identity, (hwnd, root._sumuww_native_icon_identity[0]))
            self.assertEqual(seen.setdefault(language, window), window)
        self.assertEqual(len(set(seen.values())), 3)
