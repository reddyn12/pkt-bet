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

key_list = list(const.comb)
val_list = list(const.comb.values())

driver = webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://www.espn.com/mens-college-basketball/scoreboard')
driver1 = webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver1.get("https://sportsbook.draftkings.com/leagues/basketball/3230960?category=game-lines&subcategory=game")

# do the scrapping code
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

# print(soup.div.attrs)
live_games = soup.findAll(class_="scoreboard basketball live js-show")
live_id = []
for i in live_games:
    print(i["id"])
    live_id.append(i["id"])

for i in live_id:
    driver.get("https://www.espn.com/mens-college-basketball/boxscore?gameId=" + i)

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')

    banner = soup.find(class_="competitors")
    baway = banner.find(class_="team away")
    bhome = banner.find(class_="team home")
    binfo = banner.find(class_="game-status")

    per_info = binfo.find(class_="status-detail").text
    if per_info == "Halftime":
        clock = "0"
        period = per_info
    else:
        arrper = per_info.split(" - ")
        clock = arrper[0]
        period = arrper[1]
    away_team = baway.find(class_="long-name").text
    home_team = bhome.find(class_="long-name").text

    away_score = baway.find(class_="score icon-font-after").text
    home_score = bhome.find(class_="score icon-font-before").text

    away_info = soup.find(class_="col column-one gamepackage-away-wrap")
    home_info = soup.find(class_="col column-two gamepackage-home-wrap")

    away_totals = away_info.find(class_="totals highlight")
    home_totals = home_info.find(class_="totals highlight")

    away_fgma = away_totals.find(class_="fg").text
    home_fgma = home_totals.find(class_="fg").text

    # DK START

    team_names = driver1.find_elements_by_class_name("event-cell__name")

    ps_cont = driver1.find_element_by_xpath(
        "//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[2]")

    ps_lines = ps_cont.find_elements_by_class_name("sportsbook-outcome-cell__line")
    # ps_odds=ps_cont.find_elements_by_class_name("sportsbook-odds american default-color")

    tp_cont = driver1.find_element_by_xpath(
        "//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[3]")
    tp_lines = tp_cont.find_elements_by_class_name("sportsbook-outcome-cell__line")
    # tp_odds=tp_cont.find_elements_by_class_name("sportsbook-odds american default-color")

    ml_cont = driver1.find_element_by_xpath(
        "//*[@id='root']/section/section[2]/section/div[3]/div/div[3]/div/div/div[2]/div/div[2]/div[2]/section/div[2]/div[4]")
    # ml_odds=ml_cont.find_elements_by_class_name("sportsbook-odds american default-color")

    livecnt = driver1.find_elements_by_class_name("sportsbook__icon--live")


    for x in range(len(livecnt) // 2):
        done = False
        for z in range(len(key_list)):
            naway = away_team.lower().replace(key_list[z], val_list[z]).strip()
            nhome = home_team.lower().replace(key_list[z], val_list[z]).strip()
            daway = team_names[x * 2].text.lower().strip()
            dhome = team_names[(x * 2) + 1].text.lower().strip()

            print("AWAY:  " + daway + "  |  " + naway)
            print("HOME:   " + dhome + "  |  " + nhome)
            data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                         "home_fgma": home_fgma, "away_team": away_team, "away_score": away_score,
                         "away_fgma": away_fgma, "away_ps_line": "N/A",
                         "away_tp_line": "N/A", "home_ps_line": "N/A", "home_tp_line": "N/A"}
            if (daway == naway):
                data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                             "home_fgma": home_fgma, "away_team": away_team, "away_score": away_score,
                             "away_fgma": away_fgma, "away_ps_line": ps_lines[x * 2].text,
                             "away_tp_line": tp_lines[x * 2].text, "home_ps_line": ps_lines[(x * 2) + 1].text,
                             "home_tp_line": tp_lines[(x * 2) + 1].text}
                done = True
                break
            elif (dhome == nhome):
                data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                             "home_fgma": home_fgma, "away_team": away_team, "away_score": away_score,
                             "away_fgma": away_fgma, "away_ps_line": ps_lines[x * 2].text,
                             "away_tp_line": tp_lines[x * 2].text, "home_ps_line": ps_lines[(x * 2) + 1].text,
                             "home_tp_line": tp_lines[(x * 2) + 1].text}
                done = True
                break
        if done:
            break

    # DK END

    modules.m1(data_fire["home_ps_line"],data_fire["away_ps_line"])

    db.child("ESPNcombData").child(i).push(data_fire)

driver.close()
driver1.close()
