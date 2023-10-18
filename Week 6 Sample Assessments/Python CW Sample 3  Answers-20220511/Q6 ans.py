# Ask the user if they want to begin then gather 3 numbers
# sum them then multiply by 3

def triple_three():
    num = []
    total = 0
    print("Enter 3 numbers")
    for i in range(3):
        number = input("Please enter a number: ")
        num.append(int(number))
    for item in num:
        total += item
    total *= 3
    print("The sum of the 3 numbers muliplied by 3 is %d" %total)

response = input("Shall we begin? ")
if response == 'y' or response == 'Y':
    triple_three()
else:
    print("See you later")
