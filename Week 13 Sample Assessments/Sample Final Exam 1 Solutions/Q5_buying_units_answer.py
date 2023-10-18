"""
0-1000 cost $500
1001 - 2000 cost $450
2001+ cost $420
"""


def calculate_cost(u):
    if u > unit_category_2:
        cost = unit_category_1 * price_category_1\
               + unit_category_1 * price_category_2\
               + (u - unit_category_2) * price_category_3
    elif u > unit_category_1:
        cost = unit_category_1 * price_category_1\
               + (u - unit_category_1) * price_category_2
    else:
        cost = u * price_category_1
    return cost


price_category_1 = 500
price_category_2 = 450
price_category_3 = 420

unit_category_2 = 2000
unit_category_1 = 1000

is_number = False
while not is_number:
    try:
        units = int(input('How many units do you want to purchase? '))
        is_number = True
    except:
        print('Please enter a valid whole number.')

print('Buying %d units will cost $%d.' % (units, calculate_cost(units)))
