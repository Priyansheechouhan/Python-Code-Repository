#Functions in python
#A function is a block of reusable code that performs a specific task.
#Instead of writing the same code again and again, you put it inside a function and call it whenever needed.
'''
Why use functions?

Avoid code repetition

Improve readability

Make debugging easy

Helps in modular programming
'''

#How to Create a Function in Python?
'''def function_name(parameters):
    # body of function
    return value
'''
#Example:
def greet():
    print("Hello, Priyanshee!")

#Calling function:
greet()

#Types of Functions in Python
'''We can divide functions in Python into two broad types:

1. Built-in Functions

These functions are already provided by Python.

Examples:

print()

len()

type()

input()

max()

min()

sum()

range()
'''


#User-defined Functions
#Types of user-defined functions:
#a) Function with no arguments and no return 
def greet():
    print("Hello!")
greet()

#b) Function with arguments but no return value
def greet(name):
    print("Hello", name)
greet('Priyanshee')

#c) Function with no arguments but return value
def pi_value():
    return 3.14
pi_value()

#d) Function with arguments and return value
def add(a, b):
    return a + b
add(1, 2)

#e) Function with default arguments
def greet(name="User"):
    print("Hello", name)
greet()
greet('Priyanshee')
#in this function we define default argument so if don't pass the value so it doesn't throw an error

#f) Function with variable-length arguments
# *args (Non-keyword variable arguments)
#Used when you don't know the number of arguments.
def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))   # Output: 10
#**kwargs (Keyword variable arguments)
#Used to pass key=value pairs.
def info(**details):
    print(details)

info(name="Priyanshee", age=21)

#g) Lambda Functions (Anonymous Functions)
#Small one-line functions without a name.
square = lambda x: x * x
print(square(5))

#h) Recursive Functions
#A function calling itself.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
factorial(5)

#i) Nested (Inner) Functions
#A function inside another function.
def outer():
    def inner():
        print("Inner function")
    inner()

#Practice Questions
#Basic Level

#1. Write a function to print your name.
def printname(name):
    print(name)
printname('Manush')

#2. Create a function that takes two numbers and prints their sum.
def sumoftwonumber(a, b):
    print(a + b)
sumoftwonumber(4, 5)

#3. Write a function to return the square of a number.
def returnsqure(num):
    return num ** 2
returnsqure(5)
#4. Write a function that takes your age and prints whether you are adult or not.
def checkadult(age):
    if age >= 18:
        print('Adult')
    else:
        print('Minor')
checkadult(19)

#5. Write a function with default argument country="India".
def detail(name, country='India'):
    print(f'My name is {name} and I live in {country}')
detail('Priyanshee')

#Intermediate Level
#1. Write a function that takes a list and returns the largest element.
def findLargest(nums):
    return max(nums)
findLargest([3, 4, 3, 8, 5])

#2. Create a function that counts vowels in a string.
def countvowels(string):
    vowel = 'aeiou'
    count = {}
    for ch in string:
        if ch in vowel:
            count[ch] = count.setdefault(ch, 0) + 1
    return count    
    
countvowels('Priyanshee')            

#3. Write a function using *args to calculate the product of all numbers.
def product(*numbers):
    pro = 1
    for num in numbers:
        pro *= num
    return pro
product(3, 4, 5, 1)

#4. Write a function using **kwargs to display student details.
def studentinfo(**detail):
    print(detail)

studentinfo(name = 'Priyanshee', age = 21, course = 'DS')

#5. Write a function to check if a number is prime.
def isPrime(num):
    if num <= 0:
        print('can not be prime number')
    elif num == 1:
        print('not prime nor composite')
    else:
        isprime = True
        for i in range(2, num):
            if num % i == 0:
                isprime = False
        if isprime:
            print('Prime number')
        else:
            print('not a prime number')
isPrime(-18)

#Advance Level
#1. Write a recursive function to calculate factorial.
def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)
factorial(5)

#2. Write a lambda function to check even or odd.

evenorodd = lambda num : 'even' if num%2 == 0 else 'odd'
print(evenorodd(7))

#3. Write a function to reverse a string without using slicing.
def reverseString(string):
    reverse = ''
    i = len(string) - 1
    while i >= 0:
        reverse += string[i]
        i -= 1
    return reverse
reverseString('race')   

#4. Write a function that accepts a list and returns a new list containing only even numbers.
def evenList(numbers):
    even = []
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
    return even
evenList([2, 3, 4, 5, 6, 7, 8])

#5. Write a nested function where inner function prints a message.
def outerFunction():
    def innerFunction():
        print('Hello world')
    innerFunction()
    
outerFunction()














