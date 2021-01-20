import csv
from pyexcel_io import save_data, get_data
import modules

data=get_data("stuff/ind.csv")
print(data["Brooklyn"])