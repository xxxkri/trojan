# cross platform free diskspace calculator

import ctypes
import os
import platform
import sys

dirname="/"
has_args=0

def free_space(d):
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname),None, None, ctypes.pointer(free_bytes))
        free_mb = free_bytes.value / 1024 / 1024 / 1024
        return str(free_mb) + "GB"
    else:
        st = os.statvfs(dirname)
        free_mb = st.f_bavail * st.f_frsize / 1024 / 1024 / 1024
        return str(free_mb) + "GB"

def run(**args):
    print "[*] In free_diskspace module"
    global dirname
    global has_args
    for a in args:
        has_args = 1
        dirname = args[a]
        return free_space(dirname)

    if has_args == 0:
        return free_space(dirname)

# run like this:
#print run(**{'dirname': "/home/mike"})
#print run()
