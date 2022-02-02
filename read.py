from metro import Metro
import pandas as pd

def create_cells(x):
    newcell = Metro(x[0], x[1], x[2], x[3])
    return newcell

def get_data():
	file = pd.read_table("data.csv", sep=',')
	zipp = zip(file['name'], file['code'], file['dir'], file['frequency'])
	cells = [create_cells(x) for x in zipp]
	return cells