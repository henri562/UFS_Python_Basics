# Each class has 10 x 1.5 hour tutorials
# and 7 x 1 hour lectures

def hours_classes():
   tut_and_lect = (10 * 1.5) + 7 
   return tut_and_lect

def total_hours(num_classes):
   total = hours_classes() * num_classes
   return total

# Ask the user how many classes there are
number_of_classes = int(input('How many classes are there? '))
print(total_hours(number_of_classes))


