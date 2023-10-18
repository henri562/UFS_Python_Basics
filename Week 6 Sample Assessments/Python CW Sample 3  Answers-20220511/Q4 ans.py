# Create a function that sums 3 number and doubles the result

def total_times_two(num1, num2, num3):
    total = num1 + num2 + num3
    return total*2

number1 = 4
number2 = 7
number3 = 8
dbl_sum = total_times_two(number1, number2, number3)
print("Double the sum of %d, %d and %d = %d"\
      %(number1, number2, number3, dbl_sum))
