from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

URL = 'https://www.ncaa.com/scoreboard/basketball-men/d1'
uClient = urlopen(URL)
page = uClient.read()
uClient.close()

soup = BeautifulSoup(page, 'html.parser')
games = soup.find(id='scoreboardGames')
#print(games.prettify())
live_game=games.find_all("div",class_="gamePod gamePod-type-game status-live")

for i in live_game:
    print(i,end="\n"*2)
