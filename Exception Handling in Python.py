'''
What Is Exception Handling in Python?
An exception is an error that occurs during program execution and stops the normal flow unless handled.
'''
#Example of an exception:

x = 10 / 0   # ZeroDivisionError
#Exception handling allows the program to continue running even after an error occurs.
'''
Why Use Exception Handling?

Prevent program crashes

Provide meaningful error messages

Handle expected problems (file missing, wrong input, network issues, etc.)

Python Exception Handling Blocks

Python uses 5 main keywords:

1. try

2. except

3. else

4. finally

5. raise
'''
#1. try Block
#Contains code that may cause an error.

try:
    a = int(input("Enter a number: "))
except Exception as e:
    print('find error')
    
#2. except Block
#Runs only when an exception occurs in try block.
#Example:
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
    
#3. Multiple except Blocks
#Used to handle different types of errors separately.

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number!")    
    
#4. Generic Exception (except Exception)
#Catches any error.

try:
    x = int("abc")
except Exception as e:
    print("Error occurred:", e)    
    
#5. else Block
#Runs only when no exception occurs.

try:
    num = int(input("Enter number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:", num)    
    
#6. finally Block
#Runs always, even if exception occurs or not.
#Used for cleanup code → closing files, releasing resources, disconnecting from DB.

try:
    f = open("data.txt")
    print(f.read())
except FileNotFoundError:
    print("File not found!")
finally:
    print("Execution completed.")    
    
#7. Raising Exceptions Manually → raise
#Used when you want to trigger your own error.

age = -5

if age < 0:
    raise ValueError("Age cannot be negative!")   
 
#Full Example Using ALL Blocks
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b

except ValueError:
    print("Only numbers are allowed!")

except ZeroDivisionError:
    print("Denominator cannot be zero!")

else:
    print("Result =", result)

finally:
    print("Program ended.")
    
'''
### Predefined (Built-in) Exceptions in Python
Here is the most important list used in real-world projects + interviews:

Runtime Errors
Exception	        Description
ZeroDivisionError	Division by zero
ValueError	        Wrong data type input
TypeError	        Wrong type operation (e.g., 5 + "a")
IndexError	        List/tuple index out of range
KeyError	        Wrong dictionary key
AttributeError	    Attribute does not exist
NameError	        Using variable before defining
FileNotFoundError	File does not exist
IOError	            Input/output error
ImportError	        Module not found
ModuleNotFoundError	Specific import module missing
StopIteration	    No more items in iterator
MemoryError	        Out of memory
OverflowError	    Number too large
'''

'''
### Base Exceptions
Exception       Description
Exception	    Base class for all exceptions
BaseException	Parent of all built-in exceptions
'''

#Practice Questions
#1. Handle division by zero using exception handling.
try:
    x = 10 / 0
except ZeroDivisionError as error:
    print('find error :', error)

#2. WAP to read a file. If file doesn't exist, catch the exception.
try:
    file = open('file.txt', 'r')
    print(file)
except FileNotFoundError as error:
    print(error)

#3. Write a program that takes a list and prints the 5th element. Handle IndexError.
try:
    numbers = [1, 2, 3, 4]
    print(numbers[4])
except IndexError as error:
    print(error)

#4. Create a function that accepts integer input; if user enters string, handle ValueError.
def IntegerOnly():
    try:
        num = int(input('Enter a number : '))
        print(num)
    except ValueError as error:
        print(error)
IntegerOnly()

#5. WAP to open a file and always print “Task Completed” using finally block.
try:
    file = open('file.txt', 'r')
    print(file.readall())
except FileNotFoundError as error:
    print(error)
finally:
    print('Task Completed')

#6. Create a custom exception NegativeNumberError and raise it if number < 0.
class NegativeNumberError(Exception):
    pass


try:
    num = int(input("Enter a number: "))

    if num < 0:
        raise NegativeNumberError("Number cannot be negative!")

    print("You entered:", num)

except NegativeNumberError as e:
    print("Custom Exception Caught:", e)

except ValueError:
    print("Please enter a valid integer!")
finally:
    print('Task Completed')
























