rainbow_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
my_rainbow = []
a_colour = input('Enter a colour of the rainbow:')
if a_colour in rainbow_colours:
    my_rainbow.append(a_colour)
    print(*my_rainbow)
