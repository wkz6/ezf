import win32gui, ctypes

val = win32gui.FindWindow(None, "VALORANT  ")

if not val:
    print("OPEN VALORANT")
    while not val:
        val = win32gui.FindWindow(None, "VALORANT  ")

if val:
    ctypes.windll.kernel32.ExitProcess(0)
    