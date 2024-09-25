days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

user_days = []


# a function that checks if the new day is already entered
# or if is an incorrect day
# otherwise returns True
def check_days(new_day):
    if new_day in user_days:
        print('Sorry %s is already in our list.' % new_day)
    elif new_day not in days_of_the_week:
        print('%s is not a day of the week.' % new_day)
    else:
        print('%s has been added to our days of the week.' % new_day)
        return True


for i in range(7):
    new_day = input('Enter a day of the week: ')
    # if check_days returns True add the day
    if check_days(new_day) == True:
        user_days.append(new_day)
        print(user_days)

# print a blank line - not necessary but looks better
print()
print('You have correctly entered %d days of the week.' % len(user_days))
print(user_days)
