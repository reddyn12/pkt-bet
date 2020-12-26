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
driver.get('https://www.ncaa.com/game/5773141')



# print(data)



# do the scrapping code
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
banner = soup.find(class_="gamecenter-game-banner-content")
home_info = banner.find(class_="gamecenter-game-banner-team home")
away_info = banner.find(class_="gamecenter-game-banner-team away")
mid_info = banner.find(class_="gamecenter-game-banner-scoring")
table = soup.find(class_="boxscore-table-collection")
home_team = home_info.find(class_="team-name-long").text.strip()
print(home_team)
ncid = driver.current_url[-7:]
try:
    # away_fg_box=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,"/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]"))

    away_fg_box = driver.find_element_by_xpath(
        "/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]")
    driver.execute_script("arguments[0].scrollIntoView();", away_fg_box)
    time.sleep(2)
    away_fgma = away_fg_box.text
    print("hit " + away_fgma)

except:
    away_fgma = "N/A"
    print("no hit ")

try:
    print(1)
    table_head=driver.find_element_by_class_name("boxscore-team-selector")
    print("oh")
    other_box=table_head.find_element_by_class_name("boxscore-team-selector-team homeTeam-bg-primary_color awayTeam-border-primary_color home")
    #other_box = driver.find_element_by_xpath("//*[@id='gamecenterAppContent']/div/div[1]/div[2]")
    print(2)
    driver.execute_script("arguments[0].scrollIntoView();", other_box)
    time.sleep(1)
    print(2.5)
    other_box.click()
    print(3)
    time.sleep(3)
    home_fg_box = driver.find_element_by_xpath(
        "/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]")
    driver.execute_script("arguments[0].scrollIntoView();", home_fg_box)
    time.sleep(2)
    print(5)
    home_fgma = home_fg_box.text
    print(6)
    print("hit1 " + home_fgma)
    print(7)
except:
    home_fgma = "N/A"
    print("no hit 1 ")




