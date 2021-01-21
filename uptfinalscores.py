import pyrebase
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
test=db.child("timdataNBA").get()
ids=[]
for id in test.each():
    if id.key() not in ids:
        ids.append(id.key())

for i in ids:
    pass
