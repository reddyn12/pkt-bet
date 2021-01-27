import pyrebase
import csv

import modules

tme= modules.Tme()

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
test=db.child("timdataNBA").get()
data=[["Game ID","INST ID","period","clock","home_team","home_score","home_fgm","home_fga","away_team","away_score"
                        ,"away_fgm","away_fga","away_ps_line","away_ps_odd","over_line","over_odd","home_ps_line","home_ps_odd"
                        ,"under_line","under_odd","away_ml_odd","home_ml_odd"]]
for id in test.each():
    gamedata=db.child("timdataNBA").child(id.key()).get()
    for inst in gamedata.each():
        d=inst.val()
        data.append([id.key(),inst.key(),d["period"],d["clock"],d["home_team"],d["home_score"],d["home_fgm"],d["home_fga"],d["away_team"],d["away_score"]
                        ,d["away_fgm"],d["away_fga"],d["away_ps_line"],d["away_ps_odd"],d["over_line"],d["over_odd"],d["home_ps_line"],d["home_ps_odd"]
                        ,d["under_line"],d["under_odd"],d["away_ml_odd"],d["home_ml_odd"]])


with open('output.csv', mode='w') as output_file:
    output = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in data:
        output.writerow(i)
tme.stop()
