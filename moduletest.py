import csv

import const
import modules
import matplotlib.pyplot as plt
import Row

g=0
a=0
test={}
agames=modules.gameData()
games=modules.retDataSeg(2.0,2.0,agames)
ids=[]
tim = [["Game ID", "INST ID", "period", "clock", "home_team", "home_score", "home_fgm", "home_fga", "away_team",
             "away_score"
                , "away_fgm", "away_fga", "away_ps_line", "away_ps_odd", "over_line", "over_odd", "home_ps_line",
             "home_ps_odd"
                , "under_line", "under_odd", "away_ml_odd", "home_ml_odd","Final Home Score","Final Away Score","Side to Bet","CORRECT?"]]
for i in games.keys():
    game=games.get(i)
    agame=agames.get(i)
    for j in game:
        if modules.isValidRow(j):

            if j[0] not in ids:
                ids.append(j[0])

                if "err" not in modules.m2(j):
                    a = a + 1
                    print(str(j[0])+"     "+modules.m2(j)+"     "+str(agame[-1][5])+"     "+
                      str(agame[-1][9])+"     "+str(j[16])+"     "+str(j[12])+"     "+
                          str(modules.psChecker(modules.m2(j),j,agame)))
                    tmp=j
                    tmp.append(agame[-1][5])
                    tmp.append(agame[-1][9])
                    tmp.append(modules.m2(j))
                    tmp.append(modules.psChecker(modules.m2(j),j,agame))
                    tim.append(tmp)
                    if modules.psChecker(modules.m2(j),j,agame):
                        g=g+1
                        if j[0] not in test.keys():
                            test.update({j[0]:0})
                        temp=test.get(j[0])
                        temp=temp+1
                        test.update({j[0]:temp})
with open('timmy.csv', mode='w') as output_file:
    output = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i in tim:
        output.writerow(i)
print(str(g)+"/"+str(a))
print(len(test.keys()))
