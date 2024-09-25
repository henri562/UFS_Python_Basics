"""Delivery fee -- S2 each pizza under 7 $1 for 6 - 11 pizzas 12 and over free delivery
Pizza cost 17 each pizza under 7, $15 for 6 - 11 pizzas 12 and over $13 """

pizzas = int(input('How many pizzas do you wish to order? '))

if pizzas >= 12:
    price = 17 * 6 + 15 * 5 + 13 * (pizzas - 11)
    delivery_fee = 2 * 6 + 5 * 1
elif pizzas > 6:
    price = (17 * 6) + 15 * (pizzas - 6)
    delivery_fee = (2 * 6) + 1 * (pizzas - 6)
else:
    price = pizzas * 17
    delivery_fee = pizzas * 2

total_price = price + delivery_fee

print('Your pizzas cost $%d, your delivery fee is $%d. A total cost of $%d.' % (price, delivery_fee, total_price))

''' Using function

def calc_cost(units):
    if units > 2000:
        cost = 500 * 1000 + 450 * 1000 + 420*(units-2000)
    elif units > 1000:
        cost = 500 * 1000 + 450 * (units-1000)
    else:
        cost = 500 * units
    return cost

units = int(input('How many units do you wish to purchase? '))
print('Buying %d units will cost $%d.' %(units, calc_cost(units)))

'''
