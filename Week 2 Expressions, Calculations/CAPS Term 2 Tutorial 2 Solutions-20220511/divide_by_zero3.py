x = int(input('Please enter a number: '));
y = int(input('Please enter a number to divide the first number: '));


if y == 0:
    print('You should not try to divide by zero!' )
else:
    result = x/y
    print('%.2f/%.2f = %.2f' %(x,y,result))
#    print('%.2f' %(result))
