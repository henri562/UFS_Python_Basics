# Q7 password

errors = []

lower = 0
upper = 0
numbers = 0
p = input('Type your password: ')

for char in p:
    if char.islower():
        lower += 1
    if char.isupper():
        upper += 1
    if char.isnumeric():
        numbers += 1

if len(p) < 8:
    errors.append('- Should contain at least 8 chars')
if p.isupper() or p.islower():
    errors.append('- Password must contain a mixture of lowercase and uppercase characters')
if numbers < 1:
    errors.append('- Password must contain numbers')

if p[0].lower() == 'p':
    errors.append('- Password can not start with P')

if len(errors) == 0:
    print('You have a strong password!')
else:
    print('Weak password. Please check for errors: \n')
    for error in errors:
        print(error)
