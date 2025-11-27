#Dictionary in Python
'''
A dictionary is a collection of key–value pairs.

-> Keys must be unique

-> Keys must be immutable (string, number, tuple)

-> Values can be anything

Written with { key : value }
'''
#Example
student = {
    "name": "Priyanshee",
    "age": 21,
    "skills": ["Python", "ML"]
}
print(student)

#Types of Dictionaries
#1. Normal Dictionary
d = {"a": 1, "b": 2}

#2. Nested Dictionary
d = {
    "student1": {"name": "Pri", "age": 21},
    "student2": {"name": "Chouhan", "age": 22}
}

#3. Empty Dictionary
d = {}

#4. Dictionary with tuple keys
d = {(1,2): "point"}

#Important Dictionary Methods
#Accessing Data
information = {
    'name': 'Priyanshee',
    'course' : 'DS',
    'Score' : 68    
}

#get() method
print(information.get('name'))

#keys() method
print(information.keys())

#values() method
print(information.values())

#items()
print(information.items())

#Modifying Dictionary
#update()
information.update({'age' : 21})

#pop()
print(information.pop('Score'))

#popitem
print(information.popitem())

#setdefault
information.setdefault('score', 0)
print(information)

#clear()
information.clear()
print(information)

#Looping in Dictionary
#we can iterate a dictionary via key and through a key we can get values
for key in d:
    print(key, d[key])

#but with the items() method we can access both of them 
for k, v in d.items():
    print(k, v)
    
#Practice Questions —
#Easy Level
#Create a dictionary for your details: name, age, skills.
details = {
    'name' : 'Priyanshee',
    'age' : 21,
    'skills' : ['python', 'sql', 'power bi']
    }    

print(details)

#Write code to add a new key "city": "Hyderabad" to a dictionary.
details.update({'city' : 'Hyderabad'})
print(details)
    
#Difference between get() and [] for accessing values?
print(details.get('name'))
print(details['name'])
#if key exists in the dictionary both behave same

print(details.get('Country'))
print(details['Country'])
#but if doesn't exist then get() method return none while [] throws an error

#Print all keys and values using loop.
for key in details:
    print(key)

#Medium Level
#Create a nested dictionary for 2 students.    
students_info = {
    'student1' : {
        'name' : 'Priya',
        'age' : 20,
        'course' : 'DA'
        },
    'student2' : {
        'name' : 'Rehan',
        'age' : 19,
        'course' : 'DS'
        }
    }

print(students_info)

#Update "age" in a dictionary.
students_info['student2']['age'] = 21
print(students_info['student2'])

#Remove the last inserted item using popitem().
print(students_info.popitem())

#Hard Level
#Write a program to invert a dictionary → swap keys & values.
information = {
    'name': 'Priyanshee',
    'course' : 'DS',
    'Score' : 68    
}
print(information)
inverted = {value: key for key, value in information.items()}
print(inverted)

#Count frequency of each character in a string using dictionary.
string = "Priyanshee".lower()
temp = {}

for ch in string:
    if temp.get(ch):
        temp[ch] = temp.get(ch) + 1
    else:
        temp.setdefault(ch, 1)
print(temp)

#Merge two dictionaries without using update().
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

merged = {**d1, **d2}
print(merged)






    
    