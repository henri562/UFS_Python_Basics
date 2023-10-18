toppings = []

print('Welcome to Online Rolls.')
print('You can have up to 4 toppings.')
while len(toppings) < 4:
    toppings_input = input('Please add a topping:')
    print('That will be %s' % toppings_input)
    toppings.append(toppings_input)

print('\nThank you for your order!')
print('\nYour toppings are:')

for top in toppings:
    print('. ', top)
