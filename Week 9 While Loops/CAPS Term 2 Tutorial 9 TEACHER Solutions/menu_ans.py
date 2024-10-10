menu = ['lettuce', 'cucumbers', 'tomatoes', 'onions', 'capsicums']
toppings = []


def online_rolls():
    print('Welcome to Online Rolls.')
    print('Our toppings are: lettuce, cucumbers, tomatoes, onions and capsicums.')
    response = input('Do you wish to order now? (y/n): ')
    while response == 'y':
        new_topping = input('Topping: ')
        if new_topping in menu:
            if new_topping in toppings:
                print('Sorry you have already ordered %s.' % new_topping)
                response = input('Continue to order? (y/n): ')
            else:
                print('That will be %s' % new_topping)
                toppings.append(new_topping)
                response = input('Continue to order? (y/n): ')
        else:
            print('Sorry, %s is not on our list of toppings.' % new_topping)
            response = input('Continue to order? (y/n): ')

    print('\nThank you for your order!')
    if len(toppings) > 0:
        print('\nYour toppings are: ')
        for top in toppings:
            print(top)
    else:
        print('No toppings on your roll.')


online_rolls()
