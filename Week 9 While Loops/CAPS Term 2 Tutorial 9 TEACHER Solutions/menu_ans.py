menu = ['lettuce', 'cucumbers', 'tomatoes', 'onions', 'capsicums']
toppings = []


def online_rolls():
    print('Welcome to Online Rolls.')
    print('Our toppings are: lettuce, cucumbers, tomatoes, onions and capsicums.')
    yes = input('Press y to order toppings: ')
    while yes == 'y':
        new_list = input('Topping: ')
        if new_list in menu:
            if new_list in toppings:
                print('Sorry you have already ordered %s.' % new_list)
                yes = input('Press y to order toppings: ')
            else:
                print('That will be %s' % new_list)
                toppings.append(new_list)
                yes = input('Press y to order toppings: ')
        else:
            print('Sorry not on our list of toppings.')
            yes = input('Press y to order toppings: ')

    print('\nThank you for your order!')
    if len(toppings) > 0:
        print('\nYour toppings are: ')
        for top in toppings:
            print(top)
    else:
        print('No toppings on your roll.')


online_rolls()
