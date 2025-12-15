'''
File Handling in Python

File handling allows Python programs to:

-Create files
-Read data from files
-Write data into files
-Update existing files
-Delete files

It is mainly used to store data permanently (unlike variables which store data temporarily).
Types of Files in Python

-Text files → .txt, .csv, .log
-Binary files → .dat, .bin, .jpg, .pdf

Basic File Operations
-Open a file
-Read / Write / Append
-Close the file
'''

file = open("sample.txt", "mode")

'''
File Modes
Mode	Meaning
r	    Read
w	    Write (overwrite if file exists)
a	    Append
x	    Create new file
rb	    Read binary
wb	    Write binary
'''

#Reading Files
#read() – Read entire file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

#readline() – Read one line
file = open("data.txt", "r")
print(file.readline())
file.close()

#readlines() – Read all lines as a list
file = open("data.txt", "r")
lines = file.readlines()
print(lines)
file.close()

# Writing to a File
#write() – Write text
file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("File handling example")
file.close()


# Note: w mode deletes old content.

# Appending to a File
file = open("data.txt", "a")
file.write("\nThis line is appended")
file.close()

# Using with Statement (Best Practice)

# Automatically closes the file
# Safer and cleaner

with open("data.txt", "r") as file:
    print(file.read())

# Example: Store Student Data
with open("students.txt", "w") as file:
    file.write("Name: Priyanshee\n")
    file.write("Course: Data Science\n")

# Reading File Line by Line
with open("students.txt", "r") as file:
    for line in file:
        print(line)

# Deleting a File
import os

os.remove("data.txt")

# Check If File Exists
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File not found")
    
#Practice Questions

#Basic Level
#1. Create a file hello.txt and write “Welcome to Python”.
with open("hello.txt", "w") as file:
    file.write("Welcome to Python")
    
#Read the contents of a file and print them
with open("hello.txt", "r") as file:
    print(file.read())

#Append your name to an existing file
with open("hello.txt", "a") as file:
    file.write("\nPriyanshee")

#Count the number of lines in a file
with open("hello.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))

#Read a file and display only the first line
with open("hello.txt", "r") as file:
    print(file.readline())

#INTERMEDIATE LEVEL SOLUTIONS
#Count number of words and characters
with open("hello.txt", "r") as file:
    text = file.read()
    words = len(text.split())
    characters = len(text)

print("Words:", words)
print("Characters:", characters)

#Copy content from one file to another
with open("hello.txt", "r") as source:
    with open("copy.txt", "w") as destination:
        destination.write(source.read())

#Print only lines containing the word Python
with open("hello.txt", "r") as file:
    for line in file:
        if "Python" in line:
            print(line.strip())

#Write multiple student names and read them back
students = ["Amit", "Priyanshee", "Rahul", "Neha"]

with open("students.txt", "w") as file:
    for name in students:
        file.write(name + "\n")

with open("students.txt", "r") as file:
    print(file.read())

#Find the longest line in a file
with open("students.txt", "r") as file:
    lines = file.readlines()
    longest_line = max(lines, key=len)

print("Longest line:", longest_line)

#ADVANCED LEVEL SOLUTIONS
#Store Name, Age, Marks & display students with marks > 80
with open("records.txt", "w") as file:
    file.write("Amit,20,75\n")
    file.write("Priyanshee,22,85\n")
    file.write("Neha,21,90\n")

with open("records.txt", "r") as file:
    for line in file:
        name, age, marks = line.strip().split(",")
        if int(marks) > 80:
            print(name, age, marks)

#Merge two files into a third file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    with open("merged.txt", "w") as f3:
        f3.write(f1.read())
        f3.write(f2.read())

#Remove blank lines from a file
with open("hello.txt", "r") as file:
    lines = file.readlines()

with open("hello.txt", "w") as file:
    for line in lines:
        if line.strip():
            file.write(line)

#Count how many times a word appears in a file
word = "Python"

with open("hello.txt", "r") as file:
    text = file.read()

count = text.lower().count(word.lower())
print(f"'{word}' appears {count} times")

#Menu-Driven File Handling Program
while True:
    print("\n1. Write Data")
    print("2. Read Data")
    print("3. Append Data")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        with open("menu.txt", "w") as file:
            file.write(input("Enter data: "))

    elif choice == "2":
        with open("menu.txt", "r") as file:
            print(file.read())

    elif choice == "3":
        with open("menu.txt", "a") as file:
            file.write("\n" + input("Enter data: "))

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")























