import const
import modules
import matplotlib.pyplot as plt

g=0
a=0
test={}
agames=modules.gameData()
games=modules.retDataSeg(2.0,2.0,agames)
ids=[]
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
                    if modules.psChecker(modules.m2(j),j,agame):
                        g=g+1
                        if j[0] not in test.keys():
                            test.update({j[0]:0})
                        temp=test.get(j[0])
                        temp=temp+1
                        test.update({j[0]:temp})

print(str(g)+"/"+str(a))
print(len(test.keys()))
