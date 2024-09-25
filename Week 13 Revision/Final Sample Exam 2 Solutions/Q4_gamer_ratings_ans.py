""" gamer ratings
"""

gamer_name = ['gamer123', '14Days', 'spiderman', 'bitmap123',
              'Hyper!', 'Lucky7', 'Mystic9', 'Nachos231',
              'Sceptile', 'Roadblock', 'TechWizard', 'Wolverine']

gamer_wins = [14, 50, 3, 29, 31, 0, 1, 4, 89, 1, 34, 23]

gamer_average_score = [1823, 3432, 1431, 2019, 2080, 60, 280, 2000, 3701, 200, 1500, 1400]

'''This function takes in two integers, the first one is the number
   of wins and the second one, the average score.
   The function returns the gamer rating as a string
'''


def gamer_rating(wins, score):
    if wins >= 80 and score >= 3000:
        return 'Ultimate Gamer'
    elif wins >= 20 and score >= 2000:
        return 'Super Gamer'
    elif wins >= 10 and score >= 1000:
        return 'Great Gamer'
    else:
        return 'Newbie Gamer'


for i in range(len(gamer_name)):
    print('%s %d %d %s' % (gamer_name[i], gamer_wins[i], gamer_average_score[i],
                           gamer_rating(gamer_wins[i], gamer_average_score[i])))
