'''
We will first convert fahrenheit to celsius and then We will convert celsius to fahrenheit

The formulas used in this exercise should also work in js
(js is short for javascript)

GENERAL NOTES FOR F TO C:
- 32 subtract 32
* 5/9 THEN multiply by 5/9
(100-32)*5/9 ... ie for temp of 100F to celsius

GENERAL NOTES FOR C TO F:
* 9/5 multiply by 9/5 THEN
+ 32 add 32
(5*9/5)+32 ... ie for temp of 5C to fahrenheit

5 divided by 9 is 0.555555555 ... in case need that bit of information and if use this as an exact THEN note may throw output off by a tad ... because depends on how many fives are included after the decimal
'''

# FAHRENHEIT TO CELSIUS
celsius_100 = (100-32)*5/9
print(f'\n100 Degrees Fahrenheit in Celsius: {round(celsius_100)}')
# should output 37.77777777...Celsius

celsius_0 = (0-32)*5/9
print(f'\nZERO Degrees Fahrenheit in Celsius: {round(celsius_0)}')
# should output -17.7777777 ... Celsius

print(f'\n87F Converts to', round((87 - 32)*5/9), 'Degrees Celsius')
# should output 30.55555555... Celsius

# CELSIUS TO FAHRENHEIT
fahrenheit_5 = (5*9/5)+32
print(f'\n5 Celsius in Fahrenheit: {round(fahrenheit_5)}')

fahrenheit_30 = (30*9/5)+32
print(f'\n30 Celsius in Fahrenheit: {round(fahrenheit_30)}')

print (f'\n1C Converts to Fahrenheit Temperature of', round((1*9/5)+32))