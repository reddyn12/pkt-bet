import const
import modules
import matplotlib.pyplot as plt

g=0
a=0
for name in const.teams:
    agames=modules.teamData(name)
    games=modules.retDataSeg(2.0,2.0,agames)
    ids=[]
    for i in games.keys():
        game=games.get(i)
        agame=agames.get(i)
        for j in game:
            if modules.isValidRow(j):
                if j[0] not in ids:
                    ids.append(j[0])
                    a=a+1
                    if "err" not in modules.m2(j):
                        print(name+"     "+str(j[0])+"     "+modules.m2(j)+"     "+str(agame[-1][5])+"     "+
                          str(agame[-1][9])+"     "+str(j[16])+"     "+str(j[12])+"     "+
                              str(modules.psChecker(modules.m2(j),j,agame)))
                        if modules.psChecker(modules.m2(j),j,agame):
                            g=g+1
print(str(g)+"/"+str(a))
