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
options = webdriver.ChromeOptions()
path="/Users/Nikhil/Downloads/chromedriver"
options.add_experimental_option('prefs', {
    'geolocation': True
})
driver1= webdriver.Chrome(path,options=options)

while True:
    done = False
    driver.get('https://www.espn.com/nba/scoreboard')
    driver1.get("https://sportsbook.fanduel.com/sports/navigation/830.1/10107.3")
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
        driver.get("https://www.espn.com/nba/boxscore?gameId=" + i)

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

        away_fgma = away_totals.find(class_="fg").text.split("-")
        home_fgma = home_totals.find(class_="fg").text.split("-")

        away_fgm=away_fgma[0]
        away_fga=away_fgma[1]
        home_fgm=home_fgma[0]
        home_fga=home_fgma[1]
        min=int(clock.split(":")[0])
        if(("1" in period and min<=3) or ("2" in period and min>=9)):
            data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                         "home_fgm": home_fgm, "home_fga": home_fga, "away_team": away_team, "away_score": away_score,
                         "away_fgm": away_fgm, "away_fga": away_fga, "away_ps_line": "N/A", "away_ps_odd": "N/A",
                         "over_line": "N/A", "over_odd": "N/A", "home_ps_line": "N/A", "home_ps_odd": "N/A",
                         "under_line": "N/A",
                         "under_odd": "N/A", "away_ml_odd": "N/A", "home_ml_odd": "N/A"}

            # FD START

            page1 = driver1.page_source
            soup1 = BeautifulSoup(page1, 'html.parser')

            lcont = soup1.find(class_="date live")

            lgames = lcont.findAll(class_="event")

            for a in lgames:
                names = a.findAll(class_="name")
                aname = names[0].text
                hname = names[1].text

                ps_cont = a.find(class_="market points")
                ml_cont = a.find(class_="market money")
                tot_cont = a.find(class_="market total")

                psc = ps_cont.findAll(class_="sh")
                mlc = ml_cont.findAll(class_="sh")
                totc = tot_cont.findAll(class_="sh")

                apsl = "lock"
                hpsl = "lock"
                aplo = "lock"
                hplo = "lock"

                amlo = "lock"
                hmlo = "lock"

                ototl = "lock"
                utotl = "lock"
                ototo = "lock"
                utoto = "lock"

                try:
                    apsl = psc[0].find(class_="currenthandicap").text.strip()
                    hpsl = psc[1].find(class_="currenthandicap").text.strip()
                    aplo = psc[0].find(class_="selectionprice").text.strip()
                    hplo = psc[1].find(class_="selectionprice").text.strip()
                except:
                    pass
                try:
                    amlo = mlc[0].find(class_="selectionprice").text.strip()
                    hmlo = mlc[1].find(class_="selectionprice").text.strip()
                except:
                    pass
                try:
                    ototl = totc[0].find(class_="currenthandicap").text.strip()
                    utotl = totc[1].find(class_="currenthandicap").text.strip()
                    ototo = totc[0].find(class_="selectionprice").text.strip()
                    utoto = totc[1].find(class_="selectionprice").text.strip()
                except:
                    pass
                daway=aname.lower().strip()
                dhome=hname.lower().strip()
                naway=away_team.lower().strip()
                nhome=home_team.lower().strip()

                if (naway in daway):
                    data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                                 "home_fgm": home_fgm, "home_fga": home_fga, "away_team": away_team, "away_score": away_score,
                                 "away_fgm": away_fgm, "away_fga": away_fga, "away_ps_line": apsl, "away_ps_odd": aplo,
                                 "over_line": ototl, "over_odd": ototo, "home_ps_line": hpsl, "home_ps_odd": hplo,
                                 "under_line": utotl,"under_odd": utoto, "away_ml_odd": amlo, "home_ml_odd": hmlo}
                    done = True
                    break
                elif (nhome in dhome):
                    data_fire = {"period": period, "clock": clock, "home_team": home_team, "home_score": home_score,
                                 "home_fgm": home_fgm, "home_fga": home_fga, "away_team": away_team, "away_score": away_score,
                                 "away_fgm": away_fgm, "away_fga": away_fga, "away_ps_line": apsl, "away_ps_odd": aplo,
                                 "over_line": ototl, "over_odd": ototo, "home_ps_line": hpsl, "home_ps_odd": hplo,
                                 "under_line": utotl,"under_odd": utoto, "away_ml_odd": amlo, "home_ml_odd": hmlo}
                    done = True
                    break

            # FD END

            if done:
                """
                modules.m1(data_fire["home_team"],data_fire["away_team"],data_fire["home_ps_line"],data_fire["away_ps_line"],
                           data_fire["home_fgm"],data_fire["home_fga"],data_fire["away_fgm"],data_fire["away_fga"],
                           data_fire["home_fga"],data_fire["away_fga"],data_fire["clock"],data_fire["period"])
                """
                pass

            db.child("timdataNBA").child(i).push(data_fire)
    time.sleep(30)

