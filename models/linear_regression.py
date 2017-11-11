# Linear regression assumes a linear or straight line relationship between the input variables (X) and the single output variable (y).

# A simple linear regression model follows the following formula: 
# y = b0 + b1 * x
# b0 and b1 are coeffients estimated from the training data. 

# Once the coefficients are known, use the above formula to estimate/predict the output (y)

# Steps to actually perform a linear regression:
	
# 1. Calculate the mean and the variance
# 2. Calculare the covariance
# 3. Estimate coefficients
# 4. Make the predictions

import sys
sys.path.append('..')

from utils.stats import coefficients

# Simple linear regression algorithm
def linear_regression(train, test):
  predictions = list()
  b0, b1 = coefficients(train)
  for row in test:
    yhat = b0 + b1 * row[0]
    predictions.append(yhat)
  return predictions

