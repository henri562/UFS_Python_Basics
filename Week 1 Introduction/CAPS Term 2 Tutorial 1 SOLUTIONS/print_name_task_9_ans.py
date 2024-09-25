# ask the user their name
your_name = input('What is your name? ')
your_city = input('What city are you from? ')
statement = 'Your name is ' + your_name + ' and you \
are from the city of ' + your_city + '.'
print(statement)
print()
print('Your name is %s, and you come from the city of %s.' \
      % (your_name, your_city))
