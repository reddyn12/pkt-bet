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

datafile = open('output.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
data_old = []
for row in datareader:
    data_old.append(row)
datafile.close()

driver=webdriver.Chrome("/Users/Nikhil/Downloads/chromedriver")
driver.get('https://www.ncaa.com/scoreboard/basketball-men/d1')

time.sleep(1)
page=driver.page_source
soup = BeautifulSoup(page, 'html.parser')
games = soup.find(id='scoreboardGames')

live_game=games.find_all("div",class_="gamePod gamePod-type-game status-live")
num_live_games=len(live_game)
data=[["NCAA ID","New ID","Period","Time","Home Team","Home Score","Home FGM/A","Away Team","Away Score","Away FGM/A"]]


#print(data)

for i in range(num_live_games):
    time.sleep(1)
    game_str="game-"+str(i)
    temp_game=driver.find_element_by_id(game_str)
    driver.execute_script("arguments[0].scrollIntoView();", temp_game)
    temp_game.click()
    time.sleep(1)
    # do the scrapping code
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    banner = soup.find(class_="gamecenter-game-banner-content")
    home_info = banner.find(class_="gamecenter-game-banner-team home")
    away_info = banner.find(class_="gamecenter-game-banner-team away")
    mid_info = banner.find(class_="gamecenter-game-banner-scoring")
    table = soup.find(class_="boxscore-table-collection")
    ncid = driver.current_url[-7:]
    newid = 100
    #period="FIX THIS:DEBUG"
    period = mid_info.find(class_="period").text.strip()
    try:
        clock = mid_info.find(class_="clock").text.strip()
    except:
        clock = 0


    home_team = home_info.find(class_="team-name-long").text.strip()
    home_score = mid_info.find(class_="score home").text.strip()

    home_fgma = 100
    away_team = away_info.find(class_="team-name-long").text.strip()
    away_score = mid_info.find(class_="score away").text.strip()
    try:
        #away_fg_box=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,"/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]"))

        away_fg_box=driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]")
        driver.execute_script("arguments[0].scrollIntoView();", away_fg_box)
        time.sleep(2)
        away_fgma=away_fg_box.text
        print("hit"+away_fgma)

    except:
        away_fgma="N/A"
        print("no hit")


    try:
        print(1)
        other_box=driver.find_element_by_xpath("//*[@id='gamecenterAppContent']/div/div[1]/div[2]")

        print(2)
        driver.execute_script("arguments[0].scrollIntoView();", other_box)
        time.sleep(1)
        print(2.5)
        other_box.click()
        print(3)
        time.sleep(3)
        #home_fg_box=WebDriverWait(driver,10).until(EC.presence_of_element_located(By.XPATH,"/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]"))
        home_fg_box=driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div/div[3]/div/div[2]/div/div[2]/div/table/tbody/tr[last()-1]/td[3]")
        driver.execute_script("arguments[0].scrollIntoView();", home_fg_box)
        time.sleep(2)
        print(5)
        home_fgma=home_fg_box.text
        print(6)
        print("hit1 "+home_fgma)
        print(7)
    except:
        home_fgma="N/A"
        print("no hit 1")

    child = [ncid, newid, period, clock, home_team, home_score, home_fgma, away_team, away_score, away_fgma]
    repl= False
    for j in data_old:
        if(j[0]==child[0]):
            repl=True
            j=child
    if not repl:
        data_old.insert(1,child)

    data_fire={"period":period,"clock":clock,"home_team":home_team,"home_score":home_score,"home_fgma":home_fgma,"away_team":away_team,"away_score":away_score,"away_fgma":away_fgma}
    db.child("ncaaData").child(ncid).push(data_fire)
    #end scrappin code
    driver.back()


driver.close()

autoalert.text("done scrapping", "7327541287@txt.att.net")
with open('output.csv', mode='w') as output_file:
    output = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in data_old:
        output.writerow(i)





#game=driver.find_element_by_id('game-0')
#game.click()

#data=[["NCAA ID","New ID","Period","Time","Home Team","Home Score","Home FGM","Home FGA","Away Team","Away Score","Away FGM","Away FGA",]]






"""
page=driver.page_source
soup = BeautifulSoup(page, 'html.parser')
games = soup.find(id='scoreboardGames')
#print(games.prettify())
live_game=games.find_all("div",class_="gamePod gamePod-type-game status-live")
"""


"""
for i in live_game:
    i.click()
    team_names=i.find_all("span", class_="gamePod-game-team-name")
    for j in team_names:
        print()
        #print(j.text, end="\n" * 2)

    print(i,end="\n"*2)
"""