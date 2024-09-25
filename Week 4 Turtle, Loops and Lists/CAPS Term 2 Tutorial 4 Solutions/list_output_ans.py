meals = ['breakfast', 'brunch', 'lunch', 'afternoon snack', 'dinner']
# The length is 5
print('The length is', len(meals))

meals.append('hot Chocolate')
# The length is now 6
print('The length is now', len(meals))
print('meals is', meals)

# The index of lunch is 2
print('Lunch has an index of', meals.index('lunch'))
print(meals)

# The first element after sort is afternoon snack
meals.sort()
print('Meals sorted is', meals)

# The deleted element is breakfast
del meals[1]
print('index 1 deleted leaves', meals)

# The deleted element is brunch
meals.pop(1)
print('index 1 deleted leaves', meals)

'''
# 0 is afternoon snack
1 is dinner
2 is hot choclate
3 is lunch
'''
for i in range(len(meals)):
    print(i, 'is', meals[i])

if 'brunch' not in meals:
    print('brunch is gone')
else:
    print('brunch is breakfast and lunch')
