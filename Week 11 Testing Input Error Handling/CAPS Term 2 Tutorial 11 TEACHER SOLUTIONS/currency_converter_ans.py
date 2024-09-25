# Converts Australian dollars to other currencies
currency = ['Euro', 'US Dollar', 'Singapore Dollar']
rate = [0.62, 0.71, 0.98]


# A function to test if the input is a number Returns True or False
def is_number(poss_num):
    is_num = False
    try:
        n = float(poss_num)
        is_num = True
    except:
        print('This is not a number')
    return is_num


print('Welcome!\nQuick Currency Converter can convert the following currencies.')

for i in range(3):
    print('%s. %s (%.2f)' % (str(i + 1), currency[i], rate[i]))

user_input = input('Which currency do you wish to buy (choose a number)? ')
if is_number(user_input) == False:
    print('You did not enter a number. Cannot continue.')
    exit()

num = int(user_input) - 1
if num < 0 or num > 2:
    print('Number out of range')
    exit()

amount = input('How much do you wish to exchange? ')
amount = float(amount)
if is_number(amount) == False:
    print('Impossible amount entered')
    exit()

foreign_amount = amount * rate[num]
print('Your %.2f Australian dollars is worth %.2f %ss.' % (amount, foreign_amount, currency[num]))
