# Converts Australian dollars to other currencies
#

list_heading = ['A', 'B', 'C']
currency_name = ['Euro', 'US Dollar', 'Singapore Dollar']
currency_rate = [0.62, 0.71, 0.98]


# A function to test if the input is a number
# Returns True or False
def is_number(poss_num):
    is_num = False
    try:
        n = float(poss_num)
        is_num = True
    except:
        print('This is not a number')
    return is_num


print('Welcome!\n Quick Currency Converter can convert the following currencies.')

for i in range(0, 3):
    print('%s. %s (%.2f)' % (list_heading[i], currency_name[i], currency_rate[i]))

# give the user two attempts to enter correct input (A, B or C)
attempts = 0
correct_input = False
while attempts < 2 and correct_input == False:
    attempts += 1
    user_input = input('Which currency do you wish to buy (choose a letter)? ')
    if user_input.upper() in list_heading:
        correct_input = True

if correct_input == False:
    print('You did not enter A, B, or C. Cannot continue.')
    exit()

# convert A B C to 0 1 2
currency_index = list_heading.index(user_input.upper())

# give the user two attempts to enter a number 
print('A transaction fee of $5 Australian will be applied')
attempts = 0
correct_input = False
while attempts < 2 and correct_input == False:
    attempts += 1
    amount = input('How much do you wish to exchange? ')
    if is_number(amount) == True:
        correct_input = True

if correct_input == False:
    print('Impossible amount entered')
    exit()

amount = float(amount)
foreign_amount = amount * currency_rate[currency_index]
print('Your %.2f Australian dollars (includes $5 charge) is worth %.2f %ss.' % (
    amount - 5, foreign_amount, currency_name[currency_index]))
