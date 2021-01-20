import csv

import modules

datafile = open('output.csv', 'r')
datareader = csv.reader(datafile, delimiter=',')
data = []
for row in datareader:
    data.append(row)
datafile.close()


data.pop(0)
for i in data:
    print(i[2] + "     "+i[3]+"     "+str(modules.getTime(i[2],i[3])))
