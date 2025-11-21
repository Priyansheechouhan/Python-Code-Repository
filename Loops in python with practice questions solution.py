#loops in python
#A loop is used to repeat a block of code multiple times.
#Python has two types of loops:
#1. for loop
#Used when you know how many times you want to repeat something and for iterables.
for i in range(5):
    print(i)
#When you want to iterate through a list, string, dictionary, etc.
#When repeating code fixed number of times using range().    

#2. while loop
#Used when you don’t know how many times to repeat—loop runs until condition becomes false.
count = 1
while count <= 5:
    print(count)
    count += 1
    
#Loop Control Statements    
#1. break
#Stops the loop entirely.
for i in range(10):
    if i == 5:
        break
    print(i)

#continue
#Skips the current iteration and moves to next. 
for i in range(5):
    if i == 3:
        continue
    print(i)

#pass
#Placeholder (does nothing).    
for i in range(5):
    pass

#practice questions
#Beginner Level
#Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

#Print all even numbers from 1 to 50.
for i in range(1, 51):
    if i%2 == 0:
        print(i)

#Print the characters of a string "Priyanshee" using a loop.
string = 'Priyanshee'
for ch in string:
    print(ch, end=" ")

#Find the sum of numbers from 1 to 100 using a loop.
sum_num = 0
for i in range(1, 101):
    sum_num += i

print(sum_num)

#Print the multiplication table of any number entered by user.
num = int(input('enter a number : '))
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)
    
#Intermediate Level
#Count how many vowels are in a string using a loop.
string = input('enter any word or sentence : ').lower()
count_vowels = set()

for ch in string:
    if ch in 'aeiou':
        count_vowels.add(ch)

print('count of vowels : ', len(count_vowels))

#Reverse a string using a loop (without using slicing).
string = 'hello'
ans_string = ""
i = len(string)-1
while i>=0:
    ans_string += string[i]
    i -= 1
print(ans_string)

#Find the factorial of a number using a loop.
number = int(input('enter a number : '))
fact = 1
for i in range(1, number+1):
    fact *= i
print('factorial is', fact)

#Print all elements of a list and also count them without using len().
temp = [1, 2, 3, 4, 7, 5]
count = 0
for i in temp:
    count += 1
    print(i)
print('total count is', count)

#Take 10 numbers from user and find the largest.
numbers = list(map(int, input("Enter 10 numbers : ").split()))
largest = 0
for i in numbers:
    if i > largest:
        largest = i
print('the largest from give numbers', largest)

#Advanced Level
#Check if a number is a prime number using a loop.
number = int(input('enter a number : '))
is_prime = True
if number <= 0:
    print('negative and 0 can not be prime')
elif number == 1:
    print('number is not prime nor composite')
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            
if is_prime:
    print('given number is a prime number')
else:
    print('given number is not prime')
    
#Generate the Fibonacci series up to N terms.
n = int(input('enter a number till where you want the fibonacci series : '))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[i-1] + fib[i-2])
    
for i in fib:
    print(i, end=" ")
    
#Print star triangle pattern:
for i in range(5):
    for j in range(i+1):
        print('* ', end="")
    print()
    
#Print number triangle pattern:
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

#Find duplicate elements in a list using loops (no built-in functions).
numbers = [1,1,1,2,3,4,3,5,5,8,2]
frequency = {}
for i in numbers:
    frequency[i] = frequency.get(i) + 1 if frequency.get(i) else 1
    
for k,v in frequency.items():
    if v > 1:
        print(k)