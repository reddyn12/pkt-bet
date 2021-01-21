import csv

from pyexcel_io import get_data
import matplotlib.pyplot as plt

import autoalert


def m1(ht,at,hs,ass,hp,ap,ha,aa,cl,per):
    if "1" in per:
        #8-11
        min=int(cl.split(":")[0])
        if min>=8 and min<12:
            if hs<-8.5 and hp>ap and ha>aa:
                autoalert.text()
            elif ass<-8.5 and ap>hp and aa>ha:
                autoalert.text()
    print("hi")

def lifes2short():
    pass

def lifs2long():
    pass
def teamData(name):
    data = get_data("stuff/ind.csv")
    games={}
    for i in data[name]:
        if i[0] not in games.keys():
            games.update({i[0]: []})
        d = games.get(i[0])
        d.append(i)
        games.update({i[0]: d})
    return games
def teamData1(name):
    datafile = open('output.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    data = []
    for row in datareader:
        data.append(row)
    datafile.close()
    data.pop(0)
    sort = {}

    for i in data:
        if i[4] not in sort.keys():
            sort.update({i[4]: []})
        if i[8] not in sort.keys():
            sort.update({i[8]: []})
        h = sort.get(i[4])
        a = sort.get(i[8])
        h.append(i)
        a.append(i)
        sort.update({i[4]: h})
        sort.update({i[8]: a})

    games = {}
    for i in sort.get(name):
        if i[0] not in games.keys():
            games.update({i[0]: []})
        d = games.get(i[0])
        d.append(i)
        games.update({i[0]: d})
    return games

def minconv(t):
    m=float(t.split(":")[0])
    s=float(t.split(":")[1])
    comb=720-((m*60)+s)
    sans=str(comb/720.0)
    return sans.split(".")[1]

def getTime(c,t):
    try:
        time="100"
        if t=="0":
            if "time" in c:
                time="3.0"
            else:
                if "OT" in c:
                    if "-" in c:

                        s = c.split(" - ")[0]
                        x = s.split(".")[0]
                        if len(x) == 1:
                            temp = "0:0" + x
                        else:
                            temp = "0:" + x

                        time = "5."
                        time = time + minconv(temp)
                    else:

                        time = "5.0"
                else:
                    if "-" in c:
                        perc=c.split(" - ")[1]
                        per=perc[0]
                        s=c.split(" - ")[0]
                        x=str(int(s.split(".")[0])+1)
                        if "0.0"==s:
                            time=str(int(per)+1)+".0"
                        else:
                            if len(x)==1:
                                temp = "0:0"+x
                            else:
                                temp="0:"+x
                            time=per+"."
                            time=time+minconv(temp)
                    else:
                        per=int(c[-3])
                        per=per+1
                        time=str(per)+".0"
        else:
            if "OT" in c:
                time="5."
                time=time+minconv(t)
            else:
                time=c[0]+"."
                time=time+minconv(t)

        return float(time)
    except:
        print("error timconv  "+c+"  "+t)


def m2(row):
    ans="err"
    hsd=((row[5]-row[9])+row[16])*-1
    asd=((row[9]-row[5])+row[12])*-1
    hfgp=row[6]/row[7]
    afgp=row[10]/row[11]
    hfgpa=hfgp-afgp
    afgpa=afgp-hfgp
    hfga=row[7]-row[11]
    afga=row[11]-row[7]

    if hfgpa>0 and hfga>0 and hfgpa/hfga<0.06 and hsd<-2:
        ans="home"
    elif hfgpa<0 and hfga>0 and hfgpa/hfga>-0.07 and hsd<1.5:
        ans="home"
    elif hfgpa>0 and hfga<0 and hfgpa/hfga<-0.07 and hsd<-1.5:
        ans="home"
    elif hfgpa<0 and hfga<0 and hfgpa/hfga>0.06 and hsd<2:
        ans="home"
    elif afgpa>0 and afga>0 and afgpa/afga<0.06 and asd<-2:
        ans="away"
    elif afgpa<0 and afga>0 and afgpa/afga>-0.07 and asd<1.5:
        ans="away"
    elif afgpa>0 and afga<0 and afgpa/afga<-0.07 and asd<-1.5:
        ans="away"
    elif afgpa<0 and afga<0 and afgpa/afga>0.06 and asd<2:
        ans="away"
    return ans

def pltps(name):
    games = teamData1(name)

    for i in games.keys():
        game = games.get(i)
        x = []
        y = []
        for j in game:

            if j[4] == name:
                if "." in j[16]:
                    y.append(float(j[16]))
                    x.append(getTime(j[2], j[3]))
                    # print(j[0]+": ("+str(modules.getTime(j[2], j[3]))+","+j[16])
                    # print(j[2]+"     "+j[3])
            else:
                if "." in j[12]:
                    y.append(float(j[12]))
                    x.append(getTime(j[2], j[3]))
                    # print(j[0] + ": (" + str(modules.getTime(j[2], j[3])) + "," + j[12])
                    # print(j[2] + "     " + j[3])

        plt.plot(x, y, label=i)

    plt.legend()
    plt.show()
def retDataSeg(s,e,games):
    inrange={}
    ans=[]
    for i in games.keys():
        game = games.get(i)
        for j in game:
            if getTime(str(j[2]),str(j[3]))>=s and getTime(str(j[2]),str(j[3]))<=e :
                if j[0] not in inrange.keys():
                    inrange.update({j[0]: []})
                d = inrange.get(j[0])
                d.append(j)
                inrange.update({j[0]: d})
                ans.append(getTime(str(j[2]),str(j[3])))
    return inrange