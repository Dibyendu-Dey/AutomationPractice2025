# Single Heritance
"""
Create a parent class Employee with attributes like name and salary.
Then, make a child class Manager that inherits from Employee and adds a new attribute,
such as department. The program should allow creating a manager and displaying their details.
"""


# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_employee_name(self):
        print(f"The name of the employee is {self.name}")

    def display_total_compensation(self):
        print(f"The employee's total compensation is {self.salary}")


# Child Class
class Manager(Employee):
    def __init__(self, name, salary, department):
        # Super() is used to call the constructor of the parent class.
        # It sends the data members of the child class to the parent class so it parent class initialize them.
        super().__init__(name, salary)  # this is to ensure the parent class handles the name and salary data members
        self.department = department

    def display_department(self):
        print(f"The department of employee with name {self.name} is {self.department}")


# Create an object/instance of the child class
m1 = Manager("Jharna", 900000, "Customer Support")
m1.display_employee_name()
m1.display_department()
m1.display_total_compensation()

"""
Create two parent classes:

Person – Stores name and age.
AcademicRecord – Stores grades.
Then, make a child class Student that inherits from both and adds a new attribute student_id. The program should allow creating a student and displaying their details.

Structure of the Program:
Person → Stores basic personal details.
AcademicRecord → Manages academic details.
Student (inherits from both) → Combines all attributes and displays them."""


class Person:
    """Class to restore basic personal details"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_name_age(self):
        print(f"The person's name and age is {self.name} and {self.age}")


class AcademicRecord:
    """Manages academic details"""

    def __init__(self, grade):
        self.grade = grade

    def display_grade(self):
        print(f"The obtained grade is {self.grade}")


class Student(Person, AcademicRecord):
    """Combines all attributes and displays them"""

    def __init__(self, name, age, grade, sid):
        Person.__init__(self, name, age)  # call out the constructor of the Person class.
        # It sends the name and age to the parent class to initialize them
        AcademicRecord.__init__(self, grade)  # call out the constructor of the Academic class
        self.sid = sid

    def display_sid(self):
        print(f"The id no. of {self.name} is {self.sid}")


s1 = Student("Rumi", 29, "B", 12345)
s1.display_sid()

# Multilevel inheritance: grandparent >> parent >> child
# Hierarchical inheritance: 1 Parent and multiple child
# Hybrid Inheritance: Combination of two or more inheritance

