# Q2 - Bus ticket

# calculate the price based on journeys (j)
def price_calculator(j):
    if j <= 10:
        return j * 5
    if j <= 20:
        return 50 + ((j - 10) * 4)
    return 90 + ((j - 20) * 4)


while True:
    j = input('How many journeys? ')
    if j.isnumeric():
        j = int(j)
        break
    print('Journeys\' amount must be a number')
total = price_calculator(j)
discount = (j * 5) - total
print('%d journeys costs $%d' % (j, total))
print('You received $%d as discount' % discount)
