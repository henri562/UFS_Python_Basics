animals = ['Lion', 'Dragon', 'Monkey', 'Panda']
animals.append('Tiger')
animals.sort()
for animal in animals:
    print(animal)
print()
removed_animal = animals.pop(2)
print('%s removed from list' % removed_animal)
print()
print('The length of the list is now %d.' % len(animals))
print(animals)
