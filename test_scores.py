test_scores = [80, 90, 70, 100, 67, 100]

test_scores_items = len(test_scores)
sum_of_test_scores = 0
for score in test_scores:
    sum_of_test_scores += score
    average = sum_of_test_scores/test_scores_items
print(average)

# indenting into for loop outputs iterations of the average
# indenting not included, meaning leaving the print statement at the main/outermost level outputs the final tally for average



