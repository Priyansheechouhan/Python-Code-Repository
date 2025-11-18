#what do you mean by variables in python
#A variable in Python is a name that refers to a value stored in memory.
#Think of it like a container or a labelled box where you keep some data.
#x = 10
#x → variable (name)
#10 → value stored inside it

print('-----Basics of python-----')
print('python operators')

print('arithmetic operators')
a = 5
b = 6
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)

print('assignment operators')
x = int(input('enter the number = '))
x += 3
print(x)
x -= 4
print(x)
x *= 4
print(x)
x /= 2
print(x)
x **= 2
print(x)

print('comparison/relational operators')
print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a != b)

print('logical operators')
x = int(input('enter 1st number : '))
y = int(input('enter 2nd number : '))
print(x < y and x == y)
print(x != y or x > y)
print(not (x >= y))

print('bitwise operators')
x = int(input('enter num1 : '))
y = int(input('enter num2 : '))
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << y)
print(x >> y)

print('identity operators')
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)
print(x is z)
print(x is not z)
print(x is not y)

print('membership operators')
list1 = [1, 3, 4, 6]
print(3 in list1)
print(5 in list1)
print(7 not in list1)
print(6 not in list1)

print('ternary operator')
age = 18
result = "adult" if age >= 18 else "not adult"
print(result)

print('operators precedence when we use multiple operators at single expression')
y = x * 2 / 4 + 3
print(y)
print(x)
z = 8 - 2 // 5 * 3 % 3
print(z)