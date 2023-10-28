'''
Quiz questions
'''
 
question_number=1
correct_answers=0

while question_number <= 10 and correct_answers < 3:
    the_question= 'What is '+ str(question_number) + ' * 10? '
    user_answer=input(the_question)
    try:
        if int(user_answer)== 10*question_number:
            correct_answers+=1
            print('Correct')
        else:
            print('Not correct')
    except:
        print('Not correct: You must type in a number.')
    question_number+=1

print('Thank you for doing the quiz.')
print('You answered %d questions and got %d correct answers.' \
      %(question_number-1, correct_answers))
