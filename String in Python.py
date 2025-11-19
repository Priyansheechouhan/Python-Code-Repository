# String
# Concatenating string
string = "Python"
print(string + " is a great programming language")

str1 = "Hello!!"
str2 = "Priyanshee"
print(str1 + str2)
print(str1, str2)
#String Formatting
#Old-Style Formatting (% Operator)
name = "Priyanshee"
age = 21
marks = 95.6789
print("My name is %s, I am %d years old and I scored %.2f marks." % (name, age, marks))

#str.format() Method
name = "Priyanshee"
age = 21
print("My name is {}, and I am {} years old.".format(name, age))
print("My name is {0}, I am {1} years old. {0} loves Python.".format(name, age))
print("my name is {n}, My mark is {m:.2f}".format(n = name, m = 95.2563))

#f-Strings
name = "Priyanshee"
age = 21
marks = 95.6789
print(f"My name is {name}, I am {age} years old and scored {marks} marks.")
a, b = 5, 7
print(f"The sum of {a} and {b} is {a + b}.")

#Template Strings (string.Template class)
from string import Template
t = Template("Hello, $name! You scored $marks marks.")
result = t.substitute(name="Priyanshee", marks=95)
print(result)

#Some String methods
# .isalnum() to check if the string contains alphabet and number both
string = "priyanshee123"
print(string.isalnum())

# .isalpha() to check if the string only contains alphabets 
string = "Python"
print(string.isalpha())

# .isdigit() to check if the string only contains numbers
string = '123'
print(string.isdigit())

# .capitalize() to make only first character of the word and sentence capital rest will be in lower case
string = "it is a sentence"
print(string.capitalize())

# .upper() to make all the character in the string capital form
string = "this is python programming"
print(string.upper())

# .lower() to make all characters in the string lower case
string = "Hello!! Welcome to Python world.."
print(string.lower())

#. swapcase() to swap cases like if the character is in lower case it will make it upper case and upper to lower
print(string.swapcase())

# .replace used to replace a perticular character or word in the string to other one and also can control how many occurance should change
print(string.replace('Python', 'R'))

#some basic questions
#Write a Python program to find the length of a string without using len().
string = "hello world"
print(len(string))

#Take a string input from the user and print each character on a new line.
string = input("enter you string example : ")
for ch in string:
    print(ch)
    
#Reverse a string using slicing.
string = "this is something u should learn!!"
string = string[::-1]
print(string)

#Check if a given string is a palindrome (same forward and backward).
string = "racecar"
print(string == string[::-1])

#Count the number of vowels and consonants in a string.
string = "This is the example for checking how many vowels and consonants it contains".lower()
v_count = 0
c_count = 0
for ch in string:
    if ch in 'aeiou':
        v_count += 1
    else:
        c_count += 1
print(f"total count of vowel is {v_count} and consonent is {c_count}")

#Write a program to convert a string to uppercase and lowercase.
string = "Hello World"
print(string.upper())
print(string.lower())

#Extract the first 3 and last 3 characters of a given string.
string = "Python"
print(string[0:3])
print(string[-1:-4:-1])
#join and split methods
print(':'.join(string))
#It will join the given character : to string between every character
string = "Hello this is python programming"
print(string.split())
