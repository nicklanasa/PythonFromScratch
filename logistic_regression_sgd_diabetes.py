# Logistic Regression With Stochastic Gradient Descent for Wine Quality

from random import seed
from utils.load_csv import load_csv
from utils.conversion_functions import str_column_to_float
from utils.normalize import dataset_minmax, normalize_dataset
from models.logistic_regression import logistic_regression
from evaluation_metrics.accuracy_metric import accuracy_metric
from utils.evaluate_algorithm import cv_evaluate_algorithm_with_metric_algorithm

seed(1)

filename = 'datasets/pima-indians-diabetes.csv'
dataset = load_csv(filename)

# Clean data
for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)

# Normalize
minimax = dataset_minmax(dataset)
normalize_dataset(dataset, minimax)

# Evaluate algorithm
n_folds = 5
l_rate = 0.01
n_epoch = 100
scores = cv_evaluate_algorithm_with_metric_algorithm(dataset, logistic_regression, accuracy_metric, n_folds, l_rate, n_epoch)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
