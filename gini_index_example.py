# Example of calculating Gini index

# Calculate the Gini index for a split dataset
def gini_index(groups, classes):
    # count all samples at split point
    n_instances = float(sum([len(group) for group in groups]))
    
    # sum weighted Gini index for each group
    gini = 0.0
    for group in groups:
        size = float(len(group))
        
        # avoid dividing by 0
        if size == 0:
            continue
        
        score = 0.0
        
        # score the group based on the score for each class
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        
        # weight the group score by its relative size
        gini += (1.0 - score) * (size / n_instances)
        
    return gini
    
# test Gini values
group_1 = [[[1, 1], [1, 0]], [[1, 1], [1, 0]]];
group_2 = [[[1, 0], [1, 0]], [[1, 1], [1, 1]]];

print(gini_index(group_1, [0, 1]))
print(gini_index(group_2, [0, 1]))
