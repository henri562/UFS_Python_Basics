answer_planets = 8
answer_moons = 198
answer_asteroids = 552894
planets = int(input('How many planets in the solar system?'))
if planets == answer_planets:
    moons = int(input('How many moons in the solar system?'))
    if moons == answer_moons:
        asteroids = int(input('How many asteroids in the solar system?'))
        if asteroids == answer_asteroids:
            print('Congratulations you are a winner!')
        else:
            print('Sorry, end of quiz. You answer 2 out 3 questions correctly.')
    else:
        print('Sorry end of the quiz. You answer 1 out 3 questions correctly.')
else:
    print('Sorry end of the quiz. You answer 0 out 3 questions correctly.')
