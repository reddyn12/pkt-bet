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



config = {
    "apiKey": "AIzaSyBINwiPfBLNl59Bh4GNbPAWViNfn6UZrqo",
    "authDomain": "betinfo-15db0.firebaseapp.com",
    "databaseURL": "https://betinfo-15db0-default-rtdb.firebaseio.com",
    "projectId": "betinfo-15db0",
    "storageBucket": "betinfo-15db0.appspot.com",
    "messagingSenderId": "708518271456",
    "appId": "1:708518271456:web:1a340c9103367100397385",
    "measurementId": "G-5LMCF8X1GC"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()

driver = webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://www.espn.com/mens-college-basketball/boxscore?gameId=401270544')


# do the scrapping code
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

banner=soup.find(class_="competitors")
baway=banner.find(class_="team away")
bhome=banner.find(class_="team home")
binfo=banner.find(class_="game-status")


per_info=binfo.find(class_="status-detail").text
if per_info=="Halftime":
    clock="0"
    period=per_info
else:
    arrper=per_info.split(" - ")
    clock=arrper[0]
    period=arrper[1]
away_team=baway.find(class_="long-name").text
home_team=bhome.find(class_="long-name").text

away_score=baway.find(class_="score icon-font-after").text
home_score=bhome.find(class_="score icon-font-before").text

away_info=soup.find(class_="col column-one gamepackage-away-wrap")
home_info=soup.find(class_="col column-two gamepackage-home-wrap")

away_totals=away_info.find(class_="totals highlight")
home_totals=home_info.find(class_="totals highlight")

away_fgma=away_totals.find(class_="fg").text
home_fgma=home_totals.find(class_="fg").text

print(clock)
print(period)

driver.close()