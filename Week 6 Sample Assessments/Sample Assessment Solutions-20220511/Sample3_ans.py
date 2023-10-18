birds =['Sparrow', 'Hawk','Eagle']    
print(birds)
new_bird = input('Add another bird:')

if new_bird not in birds:
    birds.append(new_bird)
    print('%s is now part of our list' % new_bird)
    print(birds)
else:
    print('Sorry only one %s is allowed in our list' % new_bird)


