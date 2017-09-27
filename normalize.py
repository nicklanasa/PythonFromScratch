from load_csv import load_csv
from utils import str_column_to_float 

def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax
	
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = (row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0])

filename = 'pima-indians-diabetes.csv'
dataset = load_csv(filename)

print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset),
    len(dataset[0])))
# convert string columns to float
for i in range(len(dataset[0])):
  str_column_to_float(dataset, i)
print(dataset[0])

# Calculate the min and max for each column 
minmax = dataset_minmax(dataset)

# Normalize columns
normalize_dataset(dataset, minmax)
print(dataset[0])
