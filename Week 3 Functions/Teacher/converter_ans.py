def converter():
   a = input('Enter a temperature in Farenheight:')
   temp_faren = int(a)
   celsius = 5/9 * (temp_faren - 32)
   celsius = int(celsius)
   print(temp_faren, 'Farenheight converted to Celsius', 'is ',celsius)

converter()
