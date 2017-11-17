# Linear Regression With Stochastic Gradient Descent for Wine Quality

from random import seed
from utils.load_csv import load_csv
from utils.conversion_functions import str_column_to_float
from utils.normalize import dataset_minmax, normalize_dataset
from models.linear_regression_sgd import linear_regression_sgd
from evaluation_metrics.rmse_metric import rmse_metric
from utils.evaluate_algorithm import cv_evaluate_algorithm_with_metric_algorithm

seed(1)

# load and prepare data
# Channel,Region,Fresh,Milk,Grocery,Frozen,Detergents_Paper,Delicassen
filename = 'datasets/wholesale_customers.csv'
dataset = load_csv(filename)

for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)

# normalize
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)

# evaluate algorithm
n_folds = 3
l_rate = 0.01
n_epoch = 50

scores = cv_evaluate_algorithm_with_metric_algorithm(dataset,
                                                     linear_regression_sgd,
                                                     rmse_metric,
                                                     n_folds,
                                                     l_rate,
                                                     n_epoch)

print('Scores: %s' % scores)
print('Mean RMSE: %.3f' % (sum(scores)/float(len(scores))))
