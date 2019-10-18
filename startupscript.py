#startup script
from subprocess import Popen
import win32gui
import time

myFil = 'LazyStartup'
windows = []


def findWindows():
    win32gui.EnumWindows(_enumW, windows)
    time.sleep(0.5)
    lookharder()
    #lookharder2() BE AFRAID VERY AFRAID

def Hwin(zz):
    win32gui.ShowWindow(zz, 0)

def Swin(zz):
    win32gui.ShowWindow(zz, 3)

def MelnickMash(hwnd):
	win32gui.DestroyWindow(hwnd)

def _enumW(hwnd, windows):
    className = win32gui.GetClassName(hwnd)
    text = win32gui.GetWindowText(hwnd)
    windows.append([hwnd, className, text])


def lookharder():
    j = -1
    for x in windows:
        j = j + 1
        if myFil in windows[j][2] or myFil == windows[j][1]:
            Hwin(windows[j][0])
            #print(windows[j][1] + windows[j][1])

def main():
	Popen(["cmd.exe", "cd c:/projects/p"])
	Popen(["start", "Stop poking me!"], shell= True)
	findWindows()
	Popen(["C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"], shell= True)
	Popen(["C:\Program Files\Sublime Text 3\sublime_text.exe"], shell=True)
	time.sleep(3)

	Popen('explorer "c:\projects\p"')
	print('You are one lazy fuck')



main()