# Linear Regression With Stochastic Gradient Descent for Wine Quality

from random import seed
from utils.load_csv import load_csv
from utils.conversion_functions import str_column_to_float
from utils.normalize import dataset_minmax, normalize_dataset
from evaluation_metrics.rmse_metric import rmse_metric
from utils.evaluate_algorithm import cv_evaluate_algorithm_with_metric_algorithm


# Make a prediction with coefficients
def predict(row, coefficients):
    yhat = coefficients[0]
    for i in range(len(row)-1):
        yhat += coefficients[i + 1] * row[i]
    return yhat


# Estimate linear regression coefficients using stochastic gradient descent
def coefficients_sgd(train, l_rate, n_epoch):
    coef = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        for row in train:
            yhat = predict(row, coef)
            error = yhat - row[-1]
            coef[0] = coef[0] - l_rate * error
            for i in range(len(row)-1):
                coef[i + 1] = coef[i + 1] - l_rate * error * row[i]
            # print(l_rate, n_epoch, error)
    return coef


# Linear Regression Algorithm With Stochastic Gradient Descent
def linear_regression_sgd(train, test, l_rate, n_epoch):
    predictions = list()
    coef = coefficients_sgd(train, l_rate, n_epoch)
    for row in test:
        yhat = predict(row, coef)
        predictions.append(yhat)
    return(predictions)


seed(1)

# load and prepare data
filename = 'datasets/winequality-white.csv'
dataset = load_csv(filename)

for i in range(len(dataset[0])):
    str_column_to_float(dataset, i)

# normalize
minmax = dataset_minmax(dataset)
normalize_dataset(dataset, minmax)

# evaluate algorithm
n_folds = 5
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
