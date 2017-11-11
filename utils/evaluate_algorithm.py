from .train_test_split import train_test_split
from .cross_validation_split import cross_validation_split

def evaluate_algorithm_with_metric_algorithm(train_dataset, test_dataset, algorithm, metric_algorithm, *args):
	test_set = list()
	for row in test_dataset:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(train_dataset, test_set, *args)
	actual = [row[-1] for row in test_dataset]
	print("=== ACTUALS ===")
	print(actual)
	print("=== PREDICTIONS ===")
	print(predicted)
	accuracy = metric_algorithm(actual, predicted)
	return accuracy

# Evaluate an algorithm using a train/test split
def tt_evaluate_algorithm_with_metric_algorithm(dataset, algorithm, metric_algorithm, split, *args):
	train, test = train_test_split(dataset, split)
	test_set = list()
	for row in test:
		row_copy = list(row)
		row_copy[-1] = None
		test_set.append(row_copy)
	predicted = algorithm(train, test_set, *args)
	actual = [row[-1] for row in test]
	print("=== ACTUALS ===")
	print(actual)
	print("=== PREDICTIONS ===")
	print(predicted)
	accuracy = metric_algorithm(actual, predicted)
	return accuracy
	
# Evaluate an algorithm using a cross validation split
def cv_evaluate_algorithm_with_metric_algorithm(dataset, algorithm, metric_algorithm, n_folds, *args):
  folds = cross_validation_split(dataset, n_folds)
  scores = list()
  for fold in folds:
    train_set = list(folds)
    train_set.remove(fold)
    train_set = sum(train_set, [])
    test_set = list()
    for row in fold:
     row_copy = list(row)
     test_set.append(row_copy)
     row_copy[-1] = None
    predicted = algorithm(train_set, test_set, *args)
    print(predicted)
    actual = [row[-1] for row in fold]
    accuracy = metric_algorithm(actual, predicted)
    scores.append(accuracy)
  return scores
