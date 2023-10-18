rainbow_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
my_rainbow = []

correct_colours=0
for i in range(len(rainbow_colours)):
    a_colour = input('Enter a colour of the rainbow: ') 
    if a_colour in rainbow_colours:
        if a_colour not in my_rainbow:
            my_rainbow.append(a_colour)
            correct_colours+=1
print(* my_rainbow, sep =', ' )

statement='You correctly entered %d colour' %correct_colours
if correct_colours!=1:
    statement+='s'
    statement+=' of the rainbow.'

print(statement)


