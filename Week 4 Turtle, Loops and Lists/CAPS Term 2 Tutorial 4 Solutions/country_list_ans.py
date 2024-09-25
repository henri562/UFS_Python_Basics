countries = ['India', 'China', 'Indonesia', 'Philippines']

new_country = input('Add a country: ')

if new_country in countries:
    print('%s is already on the list' % new_country)
else:
    countries.append(new_country)

print(countries)
