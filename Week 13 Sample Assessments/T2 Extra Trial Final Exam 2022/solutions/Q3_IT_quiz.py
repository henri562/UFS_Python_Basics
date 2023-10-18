# Q3 IT QUIZ
# case-insensitive
q = []
a = []
q.append('Short name that stands for Local Area Network: ')
a.append('LAN')
q.append('Secured Hypertext Transfer Protocol: ')
a.append('HTTPS')
q.append('The word for bullying with the use of digital technologies: ')
a.append('Cyberbullying')
correct_count = 0
question_position = 0
wrong_ans_list = []

while correct_count < 2 and len(wrong_ans_list) < 2:
    answer = input(q[question_position])
    if answer == "":
        print('Blank answer is also a wrong answer')
        wrong_ans_list.append(question_position)
    elif answer.lower() == a[question_position].lower():
        print('Correct')
        correct_count += 1
    else:
        print('Wrong')
        wrong_ans_list.append(question_position)
    question_position += 1
if correct_count == 2:
    print('Congratulations!!!')
else:
    print('You failed')
if len(wrong_ans_list) > 0:
    print('### Check the correct answers for the ones that you failed:\n')
    for i in wrong_ans_list:
        print('Question: ' + q[i])
        print('Correct answer: ' + a[i])
