# Q6 Grades
def score2grade(score):
    score = int(score)
    if score >= 85:
        return 'A'
    if score >= 70:
        return 'B'
    if score >= 50:
        return 'C'
    if score >= 40:
        return 'D'
    return 'F'


score = input('Students\' score: ')
print('%s = %s' % (score, score2grade(score)))
