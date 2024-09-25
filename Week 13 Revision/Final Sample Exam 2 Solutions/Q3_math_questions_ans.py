"""
Math questions
"""

question_number = 1
incorrect_answers = 0
correct_answers = 0

while question_number <= 10 and incorrect_answers < 3:
    the_question = 'What is ' + str(question_number) + ' squared? '
    user_answer = input(the_question)
    try:
        if int(user_answer) == question_number * question_number:
            correct_answers += 1
            print('Correct')
        else:
            print('Not correct')
            incorrect_answers += 1
    except:
        print('Not correct: You must type in a number.')
        incorrect_answers += 1
    question_number += 1

print('You answered %d questions and got %d correct answers.' \
      % (question_number - 1, correct_answers))
