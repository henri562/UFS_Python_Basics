def square(n):
  # ** Returns the square of a number
  squared = n**2
  return squared

for i in range(3,10,2):
  print('The square of %d is %d' %(i,square(i)))

