count = 0
n = 20
name = input('What is your name:')
guess_num = int(input('How many guesses do you want:'))
while count < guess_num:
    guess = int(input('Guess a number:'))
    if guess == n:
        print(' %s you are correct' % name)
        count = guess_num
    elif guess > n:
        print('Too high')
        ##                    guess = int(input('Guess again:'))
        count = count + 1
    elif guess < n:
        print('Too low')
        ##                    guess = int(input('Guess again:'))
        count = count + 1
    else:
        print('Sorry out of guesses')
