answer = input('Do you love cats? (yes or no) ')

if answer == 'yes':
    love_cats = True
else:
    love_cats = False

love_dogs = True

if love_cats == True and love_dogs == True:
    print('You love cats and dogs.')
elif love_cats == True and love_dogs == False:
    print('You love cats and not dogs.')
elif love_dogs == True:
    print('You don\'t love cats but you do love dogs.')
else:
    print('You do not love cats or dogs.')
