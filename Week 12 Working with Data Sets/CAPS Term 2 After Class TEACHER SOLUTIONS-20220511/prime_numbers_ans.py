"""
A program to find all the prime numbers
under a given number
"""

primes = []
max_number = 50

# add the first two primes as starters
primes.append(2)
primes.append(3)


def check_prime(test_number, primes):
    is_prime = True
    for p in primes:
        if test_number % p == 0:
            is_prime = False
            break
    return is_prime


number = 4
while number < max_number:
    if check_prime(number, primes) == True:
        primes.append(number)
    number += 1

for i in range(len(primes)):
    print(primes[i], end='')
    if i > 0 and (i + 1) % 10 == 0:
        print()
    elif i != len(primes) - 1:
        print(', ', end='')
    else:
        print('.')

print('There are %d primes under %d.' % (len(primes), max_number))
