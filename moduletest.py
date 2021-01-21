import modules
import matplotlib.pyplot as plt


name="LA"


games=modules.retDataSeg(3.0,3.0,modules.teamData(name))

for i in games.keys():
    game=games.get(i)
    for j in game:
        print(str(j[0])+"     "+modules.m2(j)+"     ")
