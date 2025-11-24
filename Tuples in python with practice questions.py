#Tuples in python
#A tuple is a collection of items just like a list, but:
#It is ordered
#The position of elements is fixed (index 0, 1, 2, …)
#It is immutable
#You cannot change, add, or remove elements after creating it.
#It allows duplicate values
#Just like lists.
#Created using parentheses: ()

#Syntax
my_tuple = (10, 20, 30)
#Why use Tuples?
#They are faster than lists
#Used for fixed data you don’t want to change
#Tuples can be used as keys in dictionaries (lists cannot)

#Tuple Examples
#Example 1: Basic Tuple
numbers = (10, 20, 30, 40)
print(numbers)

#Example 2: Tuple with mixed data
details = ("Priyanshee", 21, "Developer", True)
print(details)

#Example 3: Accessing elements
colors = ("red", "green", "blue")
print(colors[0])      # red
print(colors[-1])     # blue

#Example 4: Tuple inside a tuple (nested tuple)
nested = (1, 2, (3, 4, 5))
print(nested[2][1])   # 4

#Tuple Methods in Python
#Tuples have very few methods because they are immutable.

#count()
#Returns how many times a value appears in the tuple.

t = (1, 2, 2, 3, 2)
print(t.count(2))   # Output: 3

#index()
#Returns the first index of a value.

t = ("a", "b", "c", "b")
print(t.index("b"))   # Output: 1


#These are the only two main built-in methods for tuples.
#Other Useful Operations (Not Methods)
#Length of tuple
t = (10, 20, 30)
print(len(t))

#Check if an item exists
t = ("cat", "dog", "rat")
print("dog" in t)   # True

#Tuple slicing
t = (1, 2, 3, 4, 5)
print(t[1:4])   # (2, 3, 4)

#Concatenation
a = (1, 2)
b = (3, 4)
print(a + b)    # (1, 2, 3, 4)

#Repetition
t = (1, 2)
print(t * 3)    # (1, 2, 1, 2, 1, 2)

#Conversion Between List and Tuple
#Convert list → tuple
l = [1, 2, 3]
t = tuple(l)
print(t)

#Convert tuple → list
t = (1, 2, 3)
l = list(t)
print(l)

#Some practice questions
#Easy Level
#Create a tuple of 5 numbers and print the first and last element.
numbers = (1, 2, 3, 4, 5)
print(numbers[0])
print(numbers[-1])

#Create a tuple containing your name, age, and city.
info_tuple = ('priyanshee', 21, 'Hyderabad')
print(info_tuple)

#Count how many times 5 occurs in:
#(5, 2, 5, 1, 5, 3)
numbers = (5, 2, 5, 1, 5, 3)
count_5 = 0
for i in numbers:
    if i == 5:
        count_5 += 1

print('total count of 5 :', count_5)

#Find the index of "blue" in:
#("red", "green", "blue", "yellow")

colors = ("red", "green", "blue", "yellow")
print(colors.index("blue"))

#Medium Level
#Extract the middle 3 elements from this tuple:
t = (10, 20, 30, 40, 50, 60, 70)
mid = len(t) // 2
print(t[mid-1])
print(t[mid])
print(t[mid+1])

#Concatenate two tuples: (1,2,3) and (4,5,6)
tuple1 = (1,2,3)
tuple2 = (4,5,6)
temp = tuple1 + tuple2
print(temp)
#as we know tuples are immutable so we can not add one tuple another but we can store both tuples in other varibale after addding them

#Convert the tuple (100, 200, 300) into a list, add an element, and convert back to tuple.
number_tup = (100, 200, 300)
number_list = list(number_tup)
number_list.append(400)
number_tup = tuple(number_list)
print(number_tup)

#Check if "cat" exists in the tuple:
#("dog", "cat", "mouse")
animals = ("dog", "cat", "mouse")
if "cat" in animals:
    print("cat element exists in the tuple")
else:
    print("don't exists")

#Hard Level
#Given this nested tuple:
t = (1, (2, 3), (4, 5, 6), 7)
#Print the value 5.
print(t[2][1])

#Write a Python program to find the largest and smallest element in a tuple.
numbers = (2, 3, 6, 8,10,22,41)
print('minimum in the tuple :',min(numbers))
print('maximum in the tuple :',max(numbers))

#Given a tuple of numbers, count how many even numbers are inside it.
tuple_num = (2, 5, 6, 2, 9, 10, 44)
even_count = 0
for i in tuple_num:
    if i % 2 == 0:
        even_count += 1

print('even numbers count in the tuple :', even_count)



