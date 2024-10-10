count = 0
number = 20
name = input('What is your name? ')
guess_num = int(input('How many guesses do you want? '))
while count < guess_num:
    if count == 0:
        guess = int(input('Guess a number: '))
    else:
        guess = int(input('Guess again: '))
    if guess == number:
        print('%s, you are correct.' % name)
        count = guess_num
    elif guess > number:
        print('Too high.')
        count += 1
    elif guess < number:
        print('Too low.')
        count += 1
    else:
        print('Sorry out of guesses.')
