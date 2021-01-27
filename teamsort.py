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

tme= modules.Tme()
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
    d1.update({i:sort.get(i)})
save_data("stuff/ind.csv", d1)
tme.stop()





