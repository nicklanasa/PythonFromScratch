from random import seed
from random import randrange
from utils.load_csv import load_csv
from evaluation_metrics.rmse_metric import rmse_metric
from utils.evaluate_algorithm import tt_evaluate_algorithm_with_metric_algorithm
from utils.conversion_functions import str_column_to_float
from models.linear_regression import linear_regression

dataset = load_csv('datasets/insurance.csv')
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)

# dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]

rmse = tt_evaluate_algorithm_with_metric_algorithm(dataset, linear_regression, rmse_metric, 0.6)

print('RMSE: %.3f' % (rmse))
