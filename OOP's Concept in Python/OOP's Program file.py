'''#1. Class
#A class is a blueprint/template for creating objects.
#Real-life analogy
#A “Car Design Blueprint”—not a car itself, but instructions to build one.'''
#Example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def details(self):
        return f"{self.brand} {self.model}"

car1 = Car("Toyota", "Corolla")
print(car1.details())

'''2. Object (Instance)
An object is something created from a class.
If Car is the blueprint, car1 is the real car.'''
# Example
car2 = Car("Honda", "City")
print(car2.brand)      # Honda
print(car2.details())  # Honda City

'''3. Encapsulation

Encapsulation = protecting data + restricting direct access.

We use:
_variable → protected (convention)
__variable → private (name-mangled)'''

# Example
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())   # 1500

'''4. Abstraction

Abstraction means hiding complexity and providing a clean interface.
We use ABC (Abstract Base Class) and @abstractmethod.'''

# Example
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card")

p = CreditCard()
p.pay(500)

'''5. Inheritance

Inheritance = A class inherits attributes and methods of another class.
Dog inherits from Animal.'''

# Example
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark!"

d = Dog()
print(d.speak())   # Bark!
''' Multiple Inheritance
Class inherits from more than one parent.'''

# Example
class Father:
    def skill(self):
        return "Business"

class Mother:
    def skill(self):
        return "Cooking"

class Child(Father, Mother):
    pass

c = Child()
print(c.skill())   # Business (due to MRO)

'''6. Polymorphism

Polymorphism = same method name → different behaviors.'''
# Example
class Cat:
    def sound(self):
        return "Meow"

class Lion:
    def sound(self):
        return "Roar"

for animal in (Cat(), Lion()):
    print(animal.sound())

'''8. Method Overriding

Child class redefines a parent class method.'''

# Example
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")

c = Child()
c.show()

'''9. Constructor (__init__)

Runs automatically when creating an object.
'''
# Example
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

s = Student("Priyanshee", 1)
print(s.name)

'''12. Class Methods & Static Methods
 Class Method
Used for factory methods.'''

class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def total_people(cls):
        return cls.count

p1 = Person("A")
p2 = Person("B")
print(Person.total_people())  # 2

'''14. Properties (Getter/Setter)

Control attribute access using @property.'''

# Example
class Employee:
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

e = Employee(50000)
e.salary = 60000
print(e.salary)













