# Conditional statement in python
#Conditional statements allow your program to make decisions.
#They check a condition (True/False) and run different blocks of code accordingly.
#if statement
num = 4
if num < 10:
    print('number is less then 10')
    
#if-else statement
age = 18
if age >= 18 :
    print('you are an adult')
else:
    print('you are minor')    
    
#if-elif-else statement
marks = 85

if marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
else:
    print("Fail")

#Nested if (if inside another if)
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Underage")

#Practice Questions

#Easy Level
#Check if a number is positive or negative.
num = int(input("enter a number : "))
if num > 0:
    print('given number is positive')
elif num < 0:
    print('given number is negative')
else:
    print('given number is 0')

#Check if a number is odd or even.
number = int(input('enter a number : '))
if number % 2 == 0:
    print('given number is even')
else:
    print('given number is odd')

#Check if a person is eligible for voting (age >= 18).
age = int(input('enter your age : '))
if age >= 18:
    print('you are eligible for voting')
else:
    print('you are under age not eligible for voting')

#Print “Small”, “Medium”, “Large” depending on number size.
num = int(input('enter a number between 1 to 100 : '))
if num < 10:
    print('Small')
elif num < 100:
    print('Medium')
else:
    print('Large')

#Check if a character is a vowel or consonant.
ch = input('input a character : ').lower()[0]
if ch in 'aeiou':
    print('given character is vowel')
else:
    print('given character is consonant')

#Medium Level
#Input three numbers and find the largest.
num1 = int(input('enter 1st number : '))
num2 = int(input('enter 2nd number : '))
num3 = int(input('enter 3rd number : '))

if num1 > num2 :
    if num1 > num3:
        print(num1, 'is greater')
    else:
        print(num3, 'is greater')
else:
    if num2 > num3:
        print(num2, 'is greater')
    else:
        print(num3, 'is greater')

#Check whether a year is a leap year.
year = int(input('enter a year : '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('given year is a leap year')
else:
    print('not leap year')

#Check login using username & password (match strings).
username = 'admin'
password = 'admin123'

usern = input('enter the username : ')
passw = input('enter the password : ')
if usern == username:
    if passw == password:
        print('login credentials are correct')
    else:
        print('wrong password')
else:
    print('wrong username')
    
#Calculate electricity bill:
#if units ≤100 → ₹5/unit
#101–200 → ₹8/unit
#200 → ₹10/unit
units = int(input('input the unit : '))
if units <= 100:
    print('you have used power under 100 units')
    print('total bill : ', units * 5)
elif units < 200:
    print('your power consumption is between 101-200 units')
    print('total bill : ', units * 8)
else:
    print('your power consumption is more than 200 units')
    print('total bill : ', units * 10)

#Hard Level
#Write a program that checks if a number is a 3-digit number.
number = int(input('input a number : '))
length = 0
while number != 0:
    number //= 10
    length += 1
if length == 3:
    print('given number is 3-digit number')
else:
    print('not 3-digit number')

#Validate a strong password:
#≥8 chars
#contains numbers
#contains uppercase
#contains special characters
password = input("Enter your password: ")
length_ok = len(password) >= 8
number_ok = False
for ch in password:
    if ch.isdigit():
        number_ok = True
        break
uppercase_ok = False
for ch in password:
    if ch.isupper():
        uppercase_ok = True
        break
special_ok = False
for ch in password:
    if ch in "!@#$%^&*()_+-={}[]|:;'<>?,./":
        special_ok = True
        break

if length_ok and number_ok and uppercase_ok and special_ok:
    print("Strong password")
else:
    print("Password is not strong")

#Simulate a menu-driven calculator (add, sub, mul, div).
num1 = int(input('enter 1st number : '))
operator = input('input operator +,-,/,* = ')
num2 = int(input('enter 2snd number : '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '/':
    print(num1 / num2)
elif operator == '*':
    print(num1 * num2)

#Check whether a string is palindrome using conditions.
string = 'racecar'
is_palindrome = True
i = 0
j = len(string) - 1
while i < j:
    if string[i] != string[j]:
        is_palindrome = False
    i += 1
    j -= 1
if is_palindrome:
    print('given string is palindrome')
else:
    print('not palindrome')
