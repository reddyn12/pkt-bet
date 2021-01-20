import csv
from collections import OrderedDict
from pyexcel_io import save_data
import matplotlib.pyplot as plt

import modules

'''
data = OrderedDict() # from collections import OrderedDict
data.update({"Sheet 1": [[1, 2, 3], [4, 5, 6]]})
data.update({"Sheet 2": [["row 1", "row 2", "row 3"]]})
save_data("stuff/test.csv", data)
'''


datafile = open('output.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
data = []
for row in datareader:
    data.append(row)
datafile.close()
data.pop(0)
sort={}

for i in data:
    if i[4] not in sort.keys():
        sort.update({i[4]:[]})
    if i[8] not in sort.keys():
        sort.update({i[8]:[]})
    h=sort.get(i[4])
    a=sort.get(i[8])
    h.append(i)
    a.append(i)
    sort.update({i[4]: h})
    sort.update({i[8]: a})

d1=OrderedDict()
for i in sort.keys():
    print(i)
    d1.update({i:sort.get(i)})
save_data("stuff/ind.csv", d1)


games={}
tn="Brooklyn"
for i in sort.get(tn):
    if i[0] not in games.keys():
        games.update({i[0]:[]})
    d=games.get(i[0])
    d.append(i)
    games.update({i[0]:d})

for i in games.keys():
    game=games.get(i)
    x=[]
    y=[]
    for j in game:
        if j[4] == tn:
            if "." in j[16]:
                y.append(float(j[16]))
                x.append(modules.getTime(j[2], j[3]))
                print(j[0]+": ("+str(modules.getTime(j[2], j[3]))+","+j[16])
                print(j[2]+"     "+j[3])
        else:
            if "." in j[12]:
                y.append(float(j[12]))
                x.append(modules.getTime(j[2], j[3]))
                print(j[0] + ": (" + str(modules.getTime(j[2], j[3])) + "," + j[12])
                print(j[2] + "     " + j[3])

    plt.plot(x,y, label=i)

plt.legend()
plt.show()




