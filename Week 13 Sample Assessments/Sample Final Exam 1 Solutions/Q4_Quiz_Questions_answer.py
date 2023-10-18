"""
Quiz questions
"""

questions = ['4 - 16', '5 + 11', '3 x 21', '8 / 2', '3 ^ 2']
answers = [-12, 16, 63, 4, 9]

i = 0
correct = 0

while i < len(questions) and correct < 3:
    response = input('%d What is %s? ' % (i + 1, questions[i]))
    try:
        if int(response) == answers[i]:
            print('Correct.')
            correct += 1
        else:
            print('Wrong.')
    except:
        print('You didn\'t enter a whole number.')
    i += 1

print('Thank you for taking the quiz.')
print('You answered %d out of %d questions correctly.' % (correct, i))
