from metro import Metro
import pandas as pd

def create_cells(x):
	freq= x[3] + x[4] + x[5]+x[6]
	newcell = Metro(x[0], x[1], x[2], freq,x[3],x[4],x[5],x[6])
	return newcell

def get_data():
	file = pd.read_table("data.csv", sep=',')
	zipp = zip(file['Name'], file['Code'], file['Direction'], file['Q1-travels'],file['Q2-travels'],file['Q3-travels'],file['Q4-travels'])
	cells = [create_cells(x) for x in zipp]
	return cells