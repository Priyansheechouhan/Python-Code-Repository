print('1. create list of 5 elements and print first, last and middle one element')
numbers = [1, 2, 3, 4, 5]
print('first element', numbers[0])
print('last element', numbers[-1])
print('middle element', numbers[len(numbers)//2])

print('2. find the length of list without using len() function')
list1 = [2, 3, 5, 1, 9, 0]
length = 0
for i in list1:
    length += 1
print('length of given list =', length)

print('3. print only even numbers from a list')
list2 = [1, 2, 3, 4, 5, 6]
for x in list2:
    if x % 2 == 0:
        print(x)
even_numbers = [x for x in list2 if x % 2 == 0]
print(even_numbers)

print('4. print numbers greater than 10 in a list')
list3 = [9, 2, 10, 20, 40, 5]
for x in list3:
    if x > 10:
        print(x)
num_greater_10 = [x for x in list3 if x > 10]
print(num_greater_10)

print('5. find the sum of all the element in a list')
print(sum(list3))
sum = 0
for x in list3:
    sum += x
print('sum of all element =', sum)

print('6. find the maximum and minimum in a list')
list4 = [10, 20, 30, 40, 50]
max = 0
for x in list4:
    if x > max:
        max = x
print('maximum in a list =', max)

min = 0
for x in list4:
    if x < min:
        min = x
print('minimun in a list =', min)

print('7. count how many times an element appear in the list')
dict1 = {}
for x in list4:
    if dict1.get(x):
        dict1[x] = dict1.get(x) + 1
    else:
        dict1[x] = 1
print(dict1)

print('8. check whether an element exist in list or not')
list5 = [1, 2, 3, 4, 5, 6, 7, 8]
num = int(input('enter a number = '))
for x in list5:
    if x == num:
        print('element exist in the list')
        break

print('9. reverse a list without using reverse() method')
list6 = [1, 2, 3, 4, 5]
list6 = list6[::-1]
print(list6)

print('10. convert a string list into uppercase')
list_string = ['hello', 'this', 'me', 'priyanshee']
for i in range(len(list_string)):
    list_string[i] = list_string[i].upper()
print(list_string)

print('11. remove all duplicates from a list')
list7 = [1, 2, 3, 2, 2, 1, 5, 6]
list7 = list(set(list7))
print(list7)

print('12. merge two list without using +')
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

print('13. find second largest and second smalles in a list')
maximum = max(list1)
minimun = min(list1)
second_lg = 0
second_min = max(list1)

for x in list1:
    if x < maximum and x > second_lg:
        second_lg = x

    if x > minimun and x < second_min:
        second_min = x

print(second_lg)
print(second_min)
