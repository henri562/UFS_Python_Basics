# global variable
number = 0

def multiply(num1, num2):
   # print global variable
   print('Inside the function, the value of the local variable is %d.'\
         %number)
   #local variable
   product = num1 * num2 
   statement ='The value of the local variable is %d.' %product
   return statement


print(multiply(10, 20))
print('After the function, the value of the global variable is still %d.'\
      %number)
