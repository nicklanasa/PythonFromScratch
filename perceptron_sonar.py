from random import seed
from utils.load_csv import load_csv
from utils.conversion_functions import str_column_to_float, str_column_to_int
from models.perceptron import perceptron
from evaluation_metrics.accuracy_metric import accuracy_metric
from utils.evaluate_algorithm import cv_evaluate_algorithm_with_metric_algorithm


# Test the Perceptron algorithm on the sonar dataset
seed(1)

filename = 'datasets/sonar.csv'
dataset = load_csv(filename)

for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
    
# Convert string class to integers
str_column_to_int(dataset, len(dataset[0])-1)

# Evaluate algorithms
n_folds = 3
l_rate = 0.01
n_epoch = 500
scores = cv_evaluate_algorithm_with_metric_algorithm(dataset, perceptron, accuracy_metric, n_folds, l_rate, n_epoch)

print('Scores: %s' % scores)
print('Mean Accuracy %.3f%%' % (sum(scores)/float(len(scores))))
