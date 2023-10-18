# a simple comparison with if
first_number=5
second_number=first_number+7
print(first_number)
print(second_number)

# increase first_number by 7
first_number+=7
print(first_number)

# compare the numbers
if first_number==second_number:
    print('The numbers are equal')


# compare the first number with a new number
new_number=25
print()
print(first_number)
if first_number>new_number:
    print('is greater than')
else:
    print('is not greater than ')
print(new_number)
