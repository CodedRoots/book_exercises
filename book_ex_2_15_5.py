# Write a program that converts Celsius to Fahrenheit

tC = input('Enter temperature in Celsius:')
# cancelled : tF = float(tC) * 1.8 + 32
# cancelled : print('Temperature in Fahrenheit:', tF, 'F')

# Modify it from float to int
tF = int(float(tC) * 1.8 + 32)
print('Temperature in Fahrenheit:', tF, '°F')