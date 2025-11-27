#Set in Python

'''
A set in Python is an unordered collection of unique elements.

-> No duplicates

-> Unordered (no indexing)

-> Mutable (you can add/remove items)

-> Written with {}
'''

#Example
s = {1, 2, 3, 3, 4}
print(s)  #duplicate 4 will be removed

#Types of Sets
#1. Normal Set
s = {1, 2, 3}

#2. Empty Set
s = set()   # NOT {}

#3. Set with Mixed Data
s = {1, "Priyanshee", 5.6}

#4. Frozen Set (Immutable Set)
#Cannot add/remove items.
fs = frozenset([1, 2, 3])

#some common set methods
s = {1, 2, 3, 4 ,5}
s.add(6) #it is used to add the element(single item)
print(s)

s.update([7,8]) #used to add multiple items at a time
print(s)

s.remove(3) #used to remove single element if element don't exist in the set then it throws an error
print(s)

s.discard(5) #same as remove but don't throw any error if there is no such element in the set
print(s)

s.pop() #used to delete random element, don't accept any parameter
print(s)

s.clear() #used to empty the set
print(s)

#some set operations
#Union 
#add all the elements in sigle set if an element repeated it only take unique 
s1 = {1, 2, 3, 4}
s2 = {5, 6 ,7, 8}
print(s1.union(s2))
#Or we can use '|'
print(s1 | s2)

#Intersection
#only the common element from both set 
s1 = {1 , 2, 4, 3, 6, 9}
s2 = {8, 3, 5, 6, 7, 10}
print(s1.intersection(s2))
# Or we can use '&' 
print(s1 & s2)

#Difference
#it takes the element from 1st set and remove the element which are also exist in the second set
print(s1.difference(s2))
#Or we can use '-'
print(s1 - s2)

#Symmetric Difference
#it takes all element except the common element from both set
print(s1.symmetric_difference(s2))
#or we can also use '^'
print(s1 ^ s2)

#Subset Check
#used to check if 1st set is the subset of 2nd set(if s1 is a part of s2)
s1 = {3, 4, 5}
s2 = {1, 2, 3 ,4 ,5 ,6}
print(s1.issubset(s2))

#Superset
#it checks if s1 is subpart of s2
print(s2.issuperset(s1))

#Some Practice Questions
#Easy Level
#Create a set and remove duplicates from list [1,2,2,3,4,4,5].
number_list = [1,2,2,3,4,4,5]
unique_number_set = set(number_list)
print('list with duplicates :')
print(number_list)
print('set without duplicates :')
print(unique_number_set)

#Write Python code to add 10 and 20 into a set.
number = {1, 4, 12, 19}
number.update([10, 20])
print(number)

#What is the difference between remove() and discard()?
set1 = {10, 20 ,30}
set1.remove(40)
set1.discard(40)
#Both used to delete the element from the set but the only
#difference between them is if the element don't exist in the set
#remove throws an error but discard doesn't

#Create two sets and print:
#union
#intersection
#difference
set1 = {1, 2, 3, 4}
set2 = {3, 4 ,5 ,6, 7}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

#Medium Level
#Given two sets A={1,2,3,4} and B={3,4,5,6} find symmetric difference.
s1 = {1, 2, 3, 4}
s2 = {3, 4 ,5 ,6, 7}
print(s1.symmetric_difference(s2))

#Check if {1,2} is subset of {1,2,3,4}.
sub = {1, 2}
sup = {1, 2, 3, 4}
print(sub.issubset(sup))

#Convert a list into a frozen set.
l1 = [1, 2, 3, 3, 4, 2, 6, 5]
fs = frozenset(l1)
print(fs)

#Hard Level
#Write code to remove all even numbers from a set.
numbers = {1, 2 ,3 ,4 ,5 ,6 ,7,8, 9, 10}
numbers = {x for x in numbers if x%2 != 0}
print(numbers)

#Find common items in 3 sets
s1 = {1, 2, 3, 4, 5}
s2 = {3, 5, 7, 8}
s3 = {9, 8, 7, 5, 3, 2}

print(s1 & s2 & s3)

#Check if two sets are disjoint
s1 = {1, 2, 3}
s2 = {4, 5, 6}

print(s1.isdisjoint(s2))

