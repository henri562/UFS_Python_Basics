'''
A program that asks the user to type in two numbers between
1 and 20.
The second number should be bigger than the first number
'''

def one_to_twenty(number):
    if number>=1 and number<=20:
        return True
    else:
        return False
    

answer=input('Type a number between 1 and 20: ')
answer=int(answer)
if one_to_twenty(answer)==True:
    number_1=answer

answer=input('Type a number between 1 and 20 and bigger than the first number: ')
answer=int(answer)
if one_to_twenty(answer)==True:
    if answer>number_1:
        print('%d is greater than %d.' %(answer,number_1))
        print('Thank you.')


