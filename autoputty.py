import win32gui
from subprocess import Popen
import time

windows = []
j = -1
# need to detect current size of box to then act upon it
# boxes already in an array
# 

def findWindows():
    win32gui.EnumWindows(_enumW, windows)
    time.sleep(2)

def assWindow():
    


    j = 0
    for i in range(len(windows)):
        

        win32gui.MoveWindow(windows[j][0], 500, 0, 1000, 500, True)
      #  win32gui.ShowWindow(windows[1][0], 0)
    #win32gui.BringWindowToTop(windows[0][0])
        print(win32gui.IsWindowVisible(windows[0][0]))
        win32gui.SetWindowText(windows[j][0], 'Taken over your window')
    #win32gui.CreateWindow('theNEWNEW', 'BESTEST_WINDOW_EVER', 0, 200, 200, 500, 500, 0, 0, 0, 0)
        j = j + 1

def _enumW(hwnd, windows):
    className = win32gui.GetClassName(hwnd)
    text = win32gui.GetWindowText(hwnd)
    global j
    print (j)
    #if 'sublime' in className:
    if 'root@' in text:
        j = j + 1
        print (j)
        windows.append([hwnd, className, text])
        if(j == 0):
            win32gui.MoveWindow(windows[j][0], 0, 0, 500, 500, True)
        if(j == 1):
            win32gui.MoveWindow(windows[j][0], 0, 500, 500, 500, True)
        if(j == 2):
            win32gui.MoveWindow(windows[j][0], 0, 1000, 500, 500, True)
        if(j == 3):
            win32gui.MoveWindow(windows[j][0], 0, 1500, 500, 500, True)
        if(j == 4):
            win32gui.MoveWindow(windows[j][0], 0, 2000, 500, 500, True)
        if(j == 5):
            win32gui.MoveWindow(windows[j][0], 0, 2500, 500, 500, True)
        if(j == 6):
            win32gui.MoveWindow(windows[j][0], 0, 3000, 500, 500, True)



    
def main():


    Popen('putty -ssh hunter@localhost 48008 -load "Server1" -i "c:/public_key.ppk"', shell=False)
    Popen('putty -ssh hunter@localhost 20991 -load "Server2" -i "c:/public_key.ppk"', shell=True)
    Popen('putty -ssh hunter@localhost 20992 -load "Server3" -i "c:/public_key.ppk"', shell=True)
    Popen('putty -ssh hunter@localhost 20993 -load "Server4" -i "c:/public_key.ppk"', shell=True)
    Popen('putty -ssh hunter@localhost 20331 -load "Server5" -i "c:/public_key.ppk"', shell=True)
    Popen('putty -ssh hunter@localhost 24004 -load "Server6" -i "c:/public_key.ppk"', shell=True)

    time.sleep(4)
    findWindows()
#-load "session name"


main()


#hwnd = win32gui.GetForegroundWindow()
#win32gui.MoveWindow(hwnd, 0, 0, 500, 500, True)
