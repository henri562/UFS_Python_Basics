'''
Choosing between 4 different tablets
'''

price=[]
price.append(1200)
price.append(900)
price.append(700)
price.append(1050)

gigabytes=[]
gigabytes.append(144)
gigabytes.append(64)
gigabytes.append(32)
gigabytes.append(128)

# price from $800 and $1000
print('John')
print('Price, GB')
for i in range(len(price)):
    print('$%d, %d' %(price[i], gigabytes[i]), end='')
    if price[i]>=800 and price[i]<=1000:
        print('     Consider', end='')
    print()

# at least 128 GB       
print()
print('Gol')
print('Price, GB')
for i in range(len(price)):
    print('$%d, %d' %(price[i], gigabytes[i]), end='')
    if gigabytes[i]>=128:
        print('     Consider', end='')
    print()

# more than 64GB and less than $1100
print()
print('Lee')
print('Price, GB')
for i in range(len(price)):
    print('$%d, %d' %(price[i], gigabytes[i]), end='')
    if gigabytes[i]>64 and price[i]<1100:
        print('     Consider', end='')
    print()

# either less than $1000 and more than 32GB
# or more than $1000 and more than 128GB
print()
print('Ximing')
print('Price, GB')
for i in range(len(price)):
    print('$%d, %d' %(price[i], gigabytes[i]), end='')
    if gigabytes[i]>32 and price[i]<1000:
        print('     Consider', end='')
    elif gigabytes[i]>128 and price[i]>1000:
        print('     Consider', end='')
    print()

# this is another way to do Ximing
# this was not in the lecture
print()
print('Ximing')
print('Price, GB')
for i in range(len(price)):
    print('$%d, %d' %(price[i], gigabytes[i]), end='')
    if (gigabytes[i]>32 and price[i]<1000) or \
       (gigabytes[i]>128 and price[i]>1000):
        print('     Consider', end='')
    print()

