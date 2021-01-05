from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyrebase
import selenium
import autoalert
from bs4 import BeautifulSoup
import array
import time
import csv
import const
import modules
from selenium.webdriver.chrome.options import Options



options = webdriver.ChromeOptions()
path="/Users/Nikhil/Downloads/chromedriver"
options.add_experimental_option('prefs', {
    'geolocation': True
})
driver= webdriver.Chrome(path,options=options)


driver.get("https://sportsbook.fanduel.com/sports/navigation/11086.3/11087.3")

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

lcont=soup.find(class_="date live")

lgames=lcont.findAll(class_="event")

for a in lgames:
    names=a.findAll(class_="name")
    aname=names[0].text
    hname=names[1].text
    ps_cont=a.find(class_="market points")
    ml_cont=a.find(class_="market money")
    tot_cont=a.find(class_="market total")

    psc=ps_cont.findAll(class_="sh")
    mlc=ml_cont.findAll(class_="sh")
    totc=tot_cont.findAll(class_="sh")

    apsl = "lock"
    hpsl = "lock"
    aplo = "lock"
    hplo = "lock"


    amlo = "lock"
    hmlo = "lock"

    atotl = "lock"
    htotl = "lock"
    atoto = "lock"
    htoto = "lock"


    try:
        apsl=psc[0].find(class_="currenthandicap").text.strip()
        hpsl = psc[1].find(class_="currenthandicap").text.strip()
        aplo = psc[0].find(class_="selectionprice").text.strip()
        hplo = psc[1].find(class_="selectionprice").text.strip()
    except:
        pass
    try:
        amlo=mlc[0].find(class_="selectionprice").text.strip()
        hmlo=mlc[1].find(class_="selectionprice").text.strip()
    except:
        pass
    try:
        atotl=totc[0].find(class_="currenthandicap").text.strip()
        htotl=totc[1].find(class_="currenthandicap").text.strip()
        atoto=totc[0].find(class_="selectionprice").text.strip()
        htoto=totc[1].find(class_="selectionprice").text.strip()
    except:
        pass

    print(apsl+" | "+hpsl)
    print(aplo + " | " + hplo)
    print(amlo+" | "+hmlo)
    print(atotl+" | "+htotl)
    print(atoto + " | " + htoto)
    print()

driver.close()