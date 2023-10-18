six_largest_countries = ['Russia', 'Canada', 'United States', 'China',
                         'Brazil', 'Australia']
# [] is an empty list
three_largest_countries = []

while len(three_largest_countries) < 3:
    new_country = six_largest_countries.pop(0)
    print('Transferring %s' % new_country)
    # Populating the new list.    
    three_largest_countries.append(new_country)

i = 0
print('The three largest countries are:')
for country in three_largest_countries:
    i = i + 1
    print(i, country)
