from selenium import webdriver
import time
import datetime
from selenium.webdriver.chrome.options import Options
import win32gui
from subprocess import Popen


website = 'https://www.toro.com/en/customer-support/product-registration'
windows = []
myFil = 'chromedriver'
myFil2 = 'torro'
myFil3 = 'ConsoleWindowClass'
biglist = []

import socket
import sys

HOST = ''
PORT = 7000


line = ''


# Create socket on port
def reFresh():
    global line
    print('# Socket created')
    line = ''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind((HOST, PORT))
    except socket.error as msg:
        print('# Bind failed. ')
        time.sleep(5)
        reFresh()

    print('# Socket bind complete')

# Start listening on socket
    s.listen(10)
    print('# Socket now listening')

# Wait for client
    conn, addr = s.accept()
    print('# Connected to ' + addr[0] + ':' + str(addr[1]))

# Receive data from client

    data = conn.recv(1024)

    line = data.decode('UTF-8')
 # convert to string (Python 3 only)

    line = line.split('\n')   # remove newline character
    line = line.pop()
    line = line.replace('+', ' ')
    line = line.replace('%40', '@')
    line = line.split('%2C')
    p = line.pop()

    firstname, lastname, address1, address2, city, state, postalcode, country, phonenumber, email, commercialuse, ModelNumber, serialnumber, dateofpurchase, productupdatesandoffers = line

    print(line)

# add error checking on each variable to make sure the right stuff is submitted
# get rid of spaces or whatever and convert @ symbol back
# add persistence via a for loop that waits 5 seconds before restarting

    s.close()
    time.sleep(1)

    if (line != ''):
        getLoginInfo()
        time.sleep(5)
    reFresh()


def findWindows():
    win32gui.EnumWindows(_enumW, windows)
    time.sleep(0.5)
    lookharder()
    # lookharder2() BE AFRAID VERY AFRAID


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


def getLoginInfo():

    global line
    firstname, lastname, address1, address2, city, postalcode, country, state, phonenumber, email, commercialuse, ModelNumber, serialnumber, dateofpurchase, productupdatesandoffers = line
    #lastname = lastname.translate({ord(c): None for c in ' '})
    #state = state.translate({ord(c): None for c in ' '})
    #postalcode = postalcode.translate({ord(c): None for c in ' '})
    postalcode = int(postalcode)
    phonenumber = int(phonenumber)
    #if('%40' in email):
     #   a = email
     #   b = "%40"
      #  for char in b:
       # 	a = a.replace(char, " ")
      #  email = a
    browser = webdriver.Chrome()
    browser.get(website)
    time.sleep(2)

    elem1 = browser.find_element_by_name('firstname')
    elem2 = browser.find_element_by_name('lastname')
    elem3 = browser.find_element_by_name('address1')
    elem4 = browser.find_element_by_name('address2')
    elem5 = browser.find_element_by_name('city')
    elem6 = browser.find_element_by_name('postalcode')
    elem7 = browser.find_element_by_name('country')
    elem8 = browser.find_element_by_name('state')
    elem9 = browser.find_element_by_name('phonenumber')
    elem10 = browser.find_element_by_name('email')
    elem11 = browser.find_element_by_name('commercialuse')
    elem12 = browser.find_element_by_name('ModelNumber')
    elem13 = browser.find_element_by_name('serialnumber')
    elem14 = browser.find_element_by_name('dateofpurchase')
    elem15 = browser.find_element_by_id('productupdatesandoffers')
    elem16 = browser.find_element_by_id('submitForm')

    elem1.send_keys(firstname)
    elem2.send_keys(lastname)
    elem3.send_keys(address1)
    elem4.send_keys(address2)  # address 2
    elem5.send_keys(city)
    elem6.send_keys(postalcode)
    elem7.send_keys(country)
    elem8.send_keys(state)
    elem9.send_keys(phonenumber)
    elem10.send_keys(email)
    elem11.send_keys(commercialuse)
    elem12.send_keys(ModelNumber)
    elem13.send_keys(serialnumber)
    elem14.send_keys(dateofpurchase)
    elem12.click()
    elem15.click()
    elem12.click()

    time.sleep(5)
    browser.quit()

    #raise SystemExit


def main():
    reFresh()
    print('this happened')


main()

