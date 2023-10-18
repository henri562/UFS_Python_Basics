total = 0
even_total = 0
odd_total = 0
sums = input('Enter a number or "finish" to end:')
while sums != 'finish':
    # int is used here as the user can enter a string in the initial input
    num = int(sums)
    # % modulus = remainder
    if num % 2 == 0:
        even_total = even_total + num
        print('The total of even numbers is %d' % even_total)
    else:
        odd_total = odd_total + num
        print('The total of odd numbers is %d' % odd_total)
    # this input will run till the condition "finish" is met
    sums = input('Enter a number or "finish" to end:')
total = even_total + odd_total
print('The final total is %d' % total)
