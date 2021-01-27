import pyrebase
import csv

from bs4 import BeautifulSoup
from selenium import webdriver

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
driver = webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
firebase=pyrebase.initialize_app(config)

db=firebase.database()
test=db.child("timdataNBA").get()
ids=[]
for id in test.each():
    if id.key() not in ids:
        ids.append(id.key())

for i in ids:
    if "Final" not in db.child("timdataNBA").child(i).get().each()[-1].val()["period"]:

        driver.get('https://www.espn.com/nba/boxscore?gameId='+i)

        # do the scrapping code
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        #banner = soup.find(class_="competitors sm-score")
        baway = soup.find(class_="team away")
        bhome = soup.find(class_="team home")
        binfo = soup.find(class_="game-status")

        away_team = baway.find(class_="long-name").text
        home_team = bhome.find(class_="long-name").text

        away_score = baway.find(class_="score icon-font-after").text
        home_score = bhome.find(class_="score icon-font-before").text

        away_info = soup.find(class_="col column-one gamepackage-away-wrap")
        home_info = soup.find(class_="col column-two gamepackage-home-wrap")

        away_totals = away_info.findAll(class_="highlight")[0]
        home_totals = home_info.findAll(class_="highlight")[0]

        away_fgma = away_totals.find(class_="fg").text
        home_fgma = home_totals.find(class_="fg").text

        away_fgm = away_fgma[0]
        away_fga = away_fgma[1]
        home_fgm = home_fgma[0]
        home_fga = home_fgma[1]

        data_fire = {"period": "Final", "clock": "0", "home_team": home_team, "home_score": home_score,
                     "home_fgm": home_fgm, "home_fga": home_fga, "away_team": away_team, "away_score": away_score,
                     "away_fgm": away_fgm, "away_fga": away_fga, "away_ps_line": "N/A", "away_ps_odd": "N/A",
                     "over_line": "N/A", "over_odd": "N/A", "home_ps_line": "N/A", "home_ps_odd": "N/A",
                     "under_line": "N/A",
                     "under_odd": "N/A", "away_ml_odd": "N/A", "home_ml_odd": "N/A"}
        db.child("timdataNBA").child(i).push(data_fire)


driver.close()