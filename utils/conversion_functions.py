def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
		
def int_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])
		
# filename = 'pima-indians-diabetes.csv'
# dataset = load_csv(filename)
# print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset),
#   len(dataset[0])))
# print(dataset[0])

# for i in range(len(dataset[0])):
#   str_column_to_float(dataset, i)
# print(dataset[0])
