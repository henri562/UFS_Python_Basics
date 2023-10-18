"""
A program that works out Fibonacci numbers
and
makes sums100
"""

fib_num = []

# set the first two fibonacci numbers
fib_num.append(0)
fib_num.append(1)

max_number = 25000
even_sum = fib_num[0]
odd_sum = fib_num[1]

new_num = fib_num[len(fib_num) - 1] + fib_num[len(fib_num) - 2]
while new_num < max_number:
    fib_num.append(new_num)
    if new_num % 2 == 0:
        even_sum += new_num
    else:
        odd_sum += new_num
    new_num = fib_num[len(fib_num) - 1] + fib_num[len(fib_num) - 2]

print(fib_num)
print('There are %s Fibonacci numbers below %s.' % (len(fib_num), max_number))
print('The sum of the odd Fibonacci numbers under %s is %d, and the sum \
of the even numbers is %s, with a total of %s.' % (max_number, odd_sum, even_sum, odd_sum + even_sum))
