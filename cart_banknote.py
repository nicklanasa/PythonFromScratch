from random import seed
from utils.load_csv import load_csv
from utils.conversion_functions import str_column_to_float
from utils.evaluate_algorithm import cv_evaluate_algorithm_with_metric_algorithm
from evaluation_metrics.accuracy_metric import accuracy_metric
from utils.gini_index import gini_index

# Split a dataset based on an attribute and an attribute value.
def test_split(index, value, datasete):
    left, right = list(), list()
    
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
            
    return left, right
    
# Select the best split point for a dataset.
def get_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    b_index, b_value, b_score, b_groups = 999, 999, 999, None
    
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < b_score:
                b_index, b_value, b_score, b_groups = index, row[index], gini, groups
                
    return {'index': b_index, 'value': b_value, 'groups': b_groups}
    
# Create a terminal node value.
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# Create child splits for a node or make terminal
def split(node, max_depth, min_size, depth):
	left, right = node['groups']
	del(node['groups'])
	# check for a no split
	if not left or not right:
		node['left'] = node['right'] = to_terminal(left + right)
		return
	# check for max depth
	if depth >= max_depth:
		node['left'], node['right'] = to_terminal(left), to_terminal(right)
		return
	# process left child
	if len(left) <= min_size:
		node['left'] = to_terminal(left)
	else:
		node['left'] = get_split(left)
		split(node['left'], max_depth, min_size, depth+1)
	# process right child
	if len(right) <= min_size:
		node['right'] = to_terminal(right)
	else:
		node['right'] = get_split(right)
		split(node['right'], max_depth, min_size, depth+1)
 
# Build a decision tree.
def build_tree(train, max_depth, min_size):
    root = get_split(train)
    split(root, max_depth, min_size, 1)
    return root

# Make a prediction with a decision tree
def predict(node, row):
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']
            
# Classification and Regression Tree Algorithm
def decision_tree(train, test, max_depth, min_size):
    tree = build_tree(train, max_depth, min_size)
    predictions = list()
    for row in test:
        prediction = predict(tree, row)
        predictions.append(prediction)
    return(predictions)
    
# Test CART on Bank Note dataset
seed(1)

# load and prepare data
filename = 'datasets/data_banknote_authentication.csv'
dataset = load_csv(filename)

# Convert string attributes to integers
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)
    
# Evaluate algorithms
n_folds = 5
max_depth = 5
min_size = 10
scores = cv_evaluate_algorithm_with_metric_algorithm(dataset, decision_tree, accuracy_metric, n_folds, max_depth, min_size)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
