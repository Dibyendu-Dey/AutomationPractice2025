"""
We have a Base class (Employee), which provides a general implementation of calculate_salary().

The Manager class overrides this method to include performance bonuses.
The Developer class further overrides the method to include overtime pay.
"""


# The below is an example of Hierarchical inheritance - 1 Parent and Multiple Child
class Employee:  # Employee class is a blueprint that contains group of functions and data members inside a single
    # entity

    # create a constructor (init method)
    # Constructor is used to assign values to the data members of a class whenever an instance of a class is created
    def __init__(self, name, salary):  # init method
        self.name = name  # instance variable1: name
        self.salary = salary  # instance variable2: salary

    def calculate_salary(self):  # method1
        print(f"The calculated salary of employee with named {self.name} is {self.salary}")


class Manager(Employee):  # Here the Manager class is inheriting the properties of the class Employee

    def __init__(self, name, salary, perf_bonus):
        super().__init__(name, salary)
        self.perf_bonus = perf_bonus

    def calculate_salary(self):
        self.salary = self.salary + self.perf_bonus
        print(f"The calculated salary of employee with named {self.name} is {self.salary}")


class Developer(Employee):  # Here the Manager class is inheriting the properties of the class Employee

    def __init__(self, name, salary, ot_pay):
        super().__init__(name, salary)
        self.ot_pay = ot_pay

    def calculate_salary(self):
        self.salary = self.salary + self.ot_pay
        print(f"The calculated salary of employee with named {self.name} is {self.salary}")


# Let's create an object of the class Employee e1 and access the method calculate_salary
# object is a real world entity that hold certain behavior, and it instantiates the functionalities of the class.
m1 = Manager("xyz", 3200000, 100000)
m1.calculate_salary()

d1 = Manager("abc", 3200000, 100000)
d1.calculate_salary()
