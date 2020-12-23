from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyrebase
import selenium

from bs4 import BeautifulSoup
import array
import time
import csv


driver=webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get("https://sportsbook.draftkings.com/leagues/basketball/3230960?category=game-lines&subcategory=game")

config={
    "apiKey": "AIzaSyBINwiPfBLNl59Bh4GNbPAWViNfn6UZrqo",
    "authDomain": "betinfo-15db0.firebaseapp.com",
    "databaseURL": "https://betinfo-15db0-default-rtdb.firebaseio.com",
    "projectId": "betinfo-15db0",
    "storageBucket": "betinfo-15db0.appspot.com",
    "messagingSenderId": "708518271456",
    "appId": "1:708518271456:web:1a340c9103367100397385",
    "measurementId": "G-5LMCF8X1GC"
}
firebase=pyrebase.initialize_app(config)

db=firebase.database()


team_names=driver.find_elements_by_class_name("event-cell__name")

ps_cont=driver.find_element_by_xpath("//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[2]")

ps_lines=ps_cont.find_elements_by_class_name("sportsbook-outcome-cell__line")
#ps_odds=ps_cont.find_elements_by_class_name("sportsbook-odds american default-color")

tp_cont=driver.find_element_by_xpath("//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[3]")
tp_lines=tp_cont.find_elements_by_class_name("sportsbook-outcome-cell__line")
#tp_odds=tp_cont.find_elements_by_class_name("sportsbook-odds american default-color")

ml_cont=driver.find_element_by_xpath("//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[4]")
#ml_odds=ml_cont.find_elements_by_class_name("sportsbook-odds american default-color")

livecnt=driver.find_elements_by_class_name("sportsbook__icon--live")

for i in range(len(livecnt)//2):

    child={"away_team":team_names[i*2].text,"away_ps_line":ps_lines[i*2].text,"away_tp_line":tp_lines[i*2].text,"home_team":team_names[(i*2)+1].text,"home_ps_line":ps_lines[(i*2)+1].text,"home_tp_line":tp_lines[(i*2)+1].text}
    print(child)
    db.child("dk_odds").push(child)



driver.close()