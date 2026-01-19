# # ...
# class Animal:
#     def sound(self):
#         print(" Animals make sounds")

# class Dog(Animal):
#     def sound(self):
#         print("Woof!")   

# a= Animal()
# b= Dog()
# a.sound()
# b.sound()

# ##
# class BankAccount:
#     def __init__(self, owner,  balance):
#         self
#         self._balance = balance #Private attribute

#     def deposit(self, amount):
#         self._balance += amount
        
#     def get_balance(self):
#         return self._balance
    
# acc = BankAccount("Alice", 1000)
# acc.deposit(500)
# print(acc.get_balance()) # Output: 1500

# ##....
# class Student:
#     def __init__(self):
#         self.name = ""
#         self.roll_no = 0
#         self.marks = 0

#     # Method to accept student details
#     def accept_details(self):
#         self.name = input("Enter student name: ")
#         self.roll_no = int(input("Enter roll number: "))
#         self.marks = float(input("Enter marks: "))

#     # Method to display student details
#     def display_details(self):
#         print("\nStudent Details")
#         print("Name:", self.name)
#         print("Roll Number:", self.roll_no)
#         print("Marks:", self.marks)


# # Creating object of Student class
# s1 = Student()

# # Calling methods
# s1.accept_details()
# s1.display_details()


# ##
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius * self.radius

#     def circumference(self):
#         return 2 * math.pi * self.radius

# # Example usage:
# c = Circle(5)
# print("Area:", c.area())
# print("Circumference:", c.circumference())

# ##
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# # Example usage:
# e = Employee("Alice", 30, 50000)
# e.display()


# ##
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Employee(Person):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary

#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")

# # Example usage:
# e = Employee("Alice", 30, 50000)
# e.display()

# ##
# # Q4. (Inheritance)
# # Vehicle (base class) with method start()
# # Car (derived class) with method drive()
# # Create an object of Car and call both methods.

# class Vehicle:
# 	def start(self):
# 		print("Vehicle started.")

# class Car(Vehicle):
# 	def drive(self):
# 		print("Car is driving.")

# # Example usage:
# my_car = Car()
# my_car.start()  # Call base class method
# my_car.drive()  # Call derived class method

# ##
# # Q6. (Multiple Inheritance)
# # Two parent classes: Teacher and Student, each with show().
# # Derived class TeachingAssistant inherits from both and displays both messages.
# class Teacher:
# 	def show(self):
# 		print("I am a Teacher.")

# class Student:
# 	def show(self):
# 		print("I am a Student.")

# class TeachingAssistant(Teacher, Student):
# 	def show(self):
# 		Teacher.show(self)
# 		Student.show(self)

# # Example usage:
# ta = TeachingAssistant()
# ta.show()

# # Q7. (Polymorphism — Method Overriding)
# # Base class Animal with method sound(). Dog and Cat override sound().
# class Animal:
# 	def sound(self):
# 		print("Animals make sounds")

# class Dog(Animal):
# 	def sound(self):
# 		print("Woof!")

# class Cat(Animal):
# 	def sound(self):
# 		print("Meow!")

# # Example usage:
# dog = Dog()
# cat = Cat()
# dog.sound()
# cat.sound()

# # Q8. (Polymorphism — Function with Different Objects)
# # Function make_sound(animal) that calls animal.sound()
# def make_sound(animal):
# 	animal.sound()

# # Example usage:
# make_sound(dog)
# make_sound(cat)

