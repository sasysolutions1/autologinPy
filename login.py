from selenium import webdriver
import time
import datetime
from selenium.webdriver.chrome.options import Options
import win32gui
from subprocess import Popen

website = 'https://www.sendgrid.com/login'
timeLock = False
lStart = 7
lFinish = 19
windows = []
myFil = 'chromedriver'
myFil2 = 'lazylogin2'
myFil3 = 'ConsoleWindowClass'
myLog = []



# based on http://dzone.com/snippets/set-windows-desktop-wallpaper
import win32api, win32con, win32gui
 
#----------------------------------------------------------------------


InitialTime = datetime.datetime.now()
#str(InitialTime) 
#InitialTime.strftime("%Y-%m-%d %H:%M")

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
        if myFil in windows[j][2]:
            Hwin(windows[j][0])
        if myFil2 in windows[j][2] and myFil3 == windows[j][1]:
            Hwin(windows[j][0])


def lookharder2():
    j = -1
    for x in windows:
        j = j + 1
        if myFil3 in windows[j][2]:
            Hwin(windows[j][0])

def checkHour():
	timeCheck()
	time.sleep(3600)
	if(browsing == False):
		return 0


def timeCheck():
	now = datetime.datetime.now()
	#str(now) 
	#now.strftime("%Y-%m-%d %H:%M")

	if now.hour < lStart:
		print('Too Early')
		browser.quit()
		browsing = False

	if now.hour > lFinish:
		print('Too Late')
		browser.quit()
		browsing = False

	else:
		VisitSite()
		if(browsing == True):
			checkHour()


def getLoginInfo():
	

	with open('info.dat') as f:
		lines = f.readlines()
		print(lines)

		for line in lines:
			EMAIL, PWDp = line.split(' ')
			PWD, blah = PWDp.split('\n')
			detailLogin = []
			detailLogin.append(EMAIL)
			detailLogin.append(PWD)
			myLog.append(detailLogin)

	print(myLog)
	
def visitSite():
	getLoginInfo()
	myLogin = myLog[0][0]
	myPass = myLog[0][1]
	browser = webdriver.Chrome()
	browser.get(website)
	time.sleep(7)

	elem = browser.find_element_by_name('email') 
	elem1 = browser.find_element_by_name('password')

	elem.send_keys(myLogin)
	elem1.send_keys(myPass) 
	elem2 = browser.find_element_by_id('submit')

	elem2.send_keys('submit') 
	elem2.click()
	if(browser.quit ==True):
		print(browser.quit)
	
	findWindows()

def soTired():
	time.sleep(999999)
	soTired()



def main():
	browsing = True
	findWindows()

	#if(InitialTime.hour == 8 and InitialTime.year == 2017 and InitialTime.month == 4 and InitialTime.day == 15):
	#		browsing = False

		
	if (browsing == True):
		if (timeLock) == True:
			timeCheck()	
		if (timeLock) == False:
			visitSite()
			soTired()


main()