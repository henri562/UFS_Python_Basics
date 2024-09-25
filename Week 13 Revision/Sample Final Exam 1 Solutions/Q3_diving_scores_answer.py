"""
Question 3
Diving Scores
"""

name = ['Kim', 'Algi', 'Ndomo', 'Zhang', 'Raj', 'Bemet', 'Lee']
score = [9.4, 8.7, 9.1, 8.9, 9.0, 9.3, 9.5]
medal = ['Gold', 'Silver', 'Bronze']

# make a score list that is sorted in descending order
sorted_score = score.copy()
sorted_score.sort(reverse=True)

# print headers
node_length = 8
print('Diver'.ljust(node_length) + 'Dive'.ljust(node_length) + 'Medal')

# rearrange and print data
j = 0  # medal counter to track medal
k = 0  # score counter to track score
for i in range(len(score)):
    list_node = score.index(sorted_score[k])  # get index of the highest score
    k += 1

    # print scores in descending order
    if j < 3:
        print('%s%s%s' % (name[list_node].ljust(node_length), str(score[list_node]).ljust(node_length), medal[j]))
        j += 1
    else:
        print('%s%.1f' % (name[list_node].ljust(node_length), score[list_node]))
