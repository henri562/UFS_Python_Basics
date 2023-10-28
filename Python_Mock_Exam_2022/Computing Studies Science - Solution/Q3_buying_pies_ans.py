'''
50-100 cost $5
100 - 500 cost $4
500 + cost $3
'''


def calc_cost(num_units):
    if num_units > 500:
        cost=100*5+400*4+ (num_units-500)*3
    elif num_units > 100:
        cost=100*5 + (num_units-100)*4
    else:
        cost=num_units*5
    return cost
    

num_units=int(input('How many units do you wish to purchase? '))

if num_units > 50:
    cost_of_units=calc_cost(num_units)
    print('The total cost of %d pies is $%d.' %(num_units,cost_of_units))
else:
    print('Sorry, customers must order a minimum of 50 pies')
