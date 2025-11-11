'''
Write a program that asks the user for two numbers and divides the first number
by the second number. Handle any potential ZeroDivisionError or ValueError
exceptions (there is no need to retry inputs in this problem).
'''

num1 = input('Enter a number: ')
num2 = input('Enter another number: ')

try:
    result = int(num1) / int(num2)
except (ZeroDivisionError, ValueError) as e:
    print(f'Error: {e}')
else:
    print(f"result : {result}")
finally:
    print('End of program')