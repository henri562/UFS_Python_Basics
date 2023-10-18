toppings = []

print('Welcome to Online Rolls.')
print('You can have up to 4 toppings.')
quantity = int(input('How many toppings do you want:'))
while len(toppings) < quantity:
    toppings_input = input('Please add a topping:')
    print('That will be %s' % toppings_input)
    toppings.append(toppings_input)

print('\nThank you for your order!')
if len(toppings) > 0:
    print('\nYour toppings are:')
    for top in toppings:
        print('.', top)
else:
    print('No toppings on your roll.')
