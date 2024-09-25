# ask the user their name
your_name = input('What is your name? ')
your_city = input('What city are you from? ')
your_age = input('How old are you? ')
next_age = int(your_age) + 1
print('Your name is %s, you are from the city of %s.' % (your_name, your_city))
print('You are now %s years old. This time next year you will be %d years old.' \
      % (your_age, next_age))
print('One thirteenth of your current age is %.2f.' % (int(your_age) / 13))
