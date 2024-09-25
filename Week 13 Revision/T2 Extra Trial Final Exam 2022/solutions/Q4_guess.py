# Q4 Guess the number
secret = 33
wrong_count = 0
while wrong_count < 3:
    answer = input('Guess a number from 1 to 100: ')
    if not answer.isnumeric():
        print('Wrong: Only integers (whole numbers) allowed as answers')
        wrong_count += 1
    elif int(answer) > secret:
        print('Too high')
        wrong_count += 1
    elif int(answer) < secret:
        print('Too low')
        wrong_count += 1
    else:
        print('Correct')
        break
if wrong_count == 3:
    print('Out of attempts')
