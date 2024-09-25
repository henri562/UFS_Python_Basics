def add_devices(a, b, c):
    total = a + b + c
    return 'You own %d electronic devices.' % total


num_phones = int(input('How many mobile phones do you own? '))
num_computers = int(input('How many computers do you own? '))
num_tablets = int(input('How many laptops or tablets do you own? '))

print(add_devices(num_phones, num_computers, num_tablets))
