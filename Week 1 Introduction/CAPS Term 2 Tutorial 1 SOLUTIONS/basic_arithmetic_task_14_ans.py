# basic arithmetic
number_1 = input('Choose a number: ')
number_2 = input('Choose a second number: ')

number_1 = int(number_1)
number_2 = int(number_2)

print(number_1 * number_2)
print(str(number_1) + ' x ' + str(number_2) + \
      ' = ' + str(number_1 * number_2))
print(str(number_1) + '^' + str(number_2) + \
      ' = ' + str(number_1 ** number_2))
print('%d + %d = %d.' % (number_1, number_2, number_1 + number_2))
print('%d - %d = %d.' % (number_1, number_2, number_1 - number_2))
print('%d / %d = %.2f.' % (number_1, number_2, number_1 / number_2))
