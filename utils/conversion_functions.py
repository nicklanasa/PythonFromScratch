def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())
		
def int_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column])
		
def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for row in dataset:
        row[column] = lookup[row[column]]
    return lookup
		
# filename = 'pima-indians-diabetes.csv'
# dataset = load_csv(filename)
# print('Loaded data file {0} with {1} rows and {2} columns'.format(filename, len(dataset),
#   len(dataset[0])))
# print(dataset[0])

# for i in range(len(dataset[0])):
#   str_column_to_float(dataset, i)
# print(dataset[0])
