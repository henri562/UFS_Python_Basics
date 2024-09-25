def converter(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


degrees_fahrenheit = float(input('Type in the degrees Fahrenheit: '))
degrees_celsius = converter(degrees_fahrenheit)

print('%.1f Fahrenheit converted to Celsius is %.1f' \
      % (degrees_fahrenheit, degrees_celsius))
