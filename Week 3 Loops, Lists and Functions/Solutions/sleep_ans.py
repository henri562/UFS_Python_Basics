# a function with if - elif - else

def sleep_check(answer):
    if answer == 'yes':
        response = 'Have a good sleep.'
    elif answer == 'no':
        response = 'Keep studying Python.'
    else:
        response = 'Your answer must be yes or no.'
    return response


answer = input('Do you want to go to sleep? yes/no ')
print(sleep_check(answer))
