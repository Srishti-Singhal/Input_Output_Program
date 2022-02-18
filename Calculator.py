Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = input('Please enter your name: ')
print('Hello! ' + name + ', Welcome to the calculator application')
def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiplication(x,y):
    return x * y

def division(x,y):
    return x / y

def modulus(x,y):
    return x % y

print('select operation: ')
print('1. Add')
print('2. Subtract')
print('3. Multiplication')
print('4. Division')
print('5. Modulus')
choice = input('Enter choice(1/2/3/4/5): ')
num1 = float(input('Enter First Number: '))
num2 = float(input('Enter Second Number: '))
if choice == '1':
    print(num1, '+', num2 ,'=', add(num1,num2))
elif choice == '2':
    print(num1, '-', num2, '=', subtract(num1,num2))
elif choice == '3':
    print(num1, '*', num2 ,'=', multiplication(num1,num2))
elif choice == '4':
    print(num1, '/', num2 ,'=', division(num1,num2))
elif choice == '5':
    print(num1, '%', num2 ,'=', modulus(num1,num2))    
else:
    print('Invalid Input')
