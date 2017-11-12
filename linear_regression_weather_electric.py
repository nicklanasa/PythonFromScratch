from utils.load_csv import load_csv
from evaluation_metrics.rmse_metric import rmse_metric
from utils.evaluate_algorithm import tt_evaluate_algorithm_with_metric_algorithm, evaluate_algorithm_with_metric_algorithm
from utils.conversion_functions import int_column_to_float
from models.linear_regression import linear_regression

dataset = load_csv('datasets/electrical_output_weather.csv')
test_dataset = load_csv('datasets/test_electrical_output_weather.csv')

for i in range(len(dataset[0])):
    int_column_to_float(dataset, i)

for i in range(len(test_dataset[0])):
    int_column_to_float(test_dataset, i)

# rmse = tt_evaluate_algorithm_with_metric_algorithm(dataset,
#                                                    linear_regression,
#                                                    rmse_metric,
#                                                    0.6)

rmse = evaluate_algorithm_with_metric_algorithm(dataset,
                                                test_dataset,
                                                linear_regression,
                                                rmse_metric)

print('RMSE: %.3f' % (rmse))
