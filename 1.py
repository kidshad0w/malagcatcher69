from unittest import skip
from bs4 import BeautifulSoup
import requests
import re
import selenium
import pyautogui
import time


from selenium import webdriver
#opens browers#
browser = webdriver.Edge(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe")

browser.get('https://students.technion.ac.il/login/index.php')

while True:
    time.sleep(3)
    print(pyautogui.position())

time.sleep(5)
pyautogui.click(x=1077, y=538)

time.sleep(4)
pyautogui.click(x=532, y=630)
time.sleep(2)
print(pyautogui.position())

#converts course lists into meaningful values#
with open("malag.txt","r", encoding="utf-8") as f:
    mlglist=[]
    for line in f:
        for malagnum in line.split(" "):
            try:
                temp=str(malagnum)
                if len(temp)<5:
                    continue
                else:
                    mlglist.append(int(malagnum))
            except ValueError or TypeError or SyntaxError or UnicodeDecodeError:
                None
print(mlglist)

#gets page source and tells me if available, needs fixing#
'''
for i in range(len(mlglist[:1])):
    url = f"https://students.technion.ac.il/local/technionsearch/course/{str(mlglist[i])}#s_202102"
    page = str(mlglist[i])

    req = requests.get(url, 'html.parser')

    with open(page, 'w', encoding="utf-8") as f:
        f.write(req.text)
        f.close()
    temppage = BeautifulSoup(req.text, 'html.parser')
    xtemp=temppage.find_all("div")
    print(temppage.prettify)
'''
'''    for i in xtemp:
        print(i)
        if (i.string == "םייונפ תומוקמ ןיא"):
                    print(page+" out of places")
        if (i.get('class')=="text-muted"):
            print(i)
            print('k')
            if (i.get('role')=="alert"):
                print(page, i)
                
                if (i.string == "םייונפ תומוקמ ןיא"):
                    print(page+" out of places")
                else:
                    print("check " + page)
    '''