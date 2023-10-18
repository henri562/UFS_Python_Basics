count = 0
even_total = 0
average = 0
sums = input('Enter an even number or "finish" to end:')
while sums != 'finish':
    # int is used here as the user can enter a string in the initial input
    num = int(sums)
    # % modulas = divide
    if num % 2 == 0:
        even_total = even_total + num
        print('The total of even numbers is %d' % even_total)
        count = count + 1
        average = (even_total / count)
    else:
        print('Sorry we only accept even numbers')
    # this input will run till the condition "finish" is met
    sums = input('Enter an even number or "finish" to end:')

print('The final total is %d' % even_total)
print('The average is %d' % average)
