"""
Create a class with name Student having the below data members and member functions:
Class name: Student
Data Members: SName, SRollNo, Branch, DOB
Member Functions: Read, Write, Play
"""


# use the class keyword to define a class in Python
class Student:  # class is a blueprint which contains group of functions and data members inside a single entity
    # Define the data members as class variables:
    def __init__(self, s_name, s_roll_no, branch, DOB):
        # constructor or init method is used to assign values to data members when an object of the class is created
        self.s_name = s_name
        self.s_roll_no = s_roll_no
        self.branch = branch
        self.DOB = DOB
    # NOTE: class variables can be accessed using Class name
    # Data members are the variables or attributes that hold the data of an instance of a variable. These variables are
    # associated with the object created from the class and represent the properties of the class

    # Member Functions:
    # self is a default parameter that holds the address of the data members or parameters passed to the method
    def read(self):
        print(f"{self.s_name} is reading.")

    def write(self):
        print(f"{self.s_name} is writing.")

    def play(self):
        print(f"{self.s_name} is playing.")


# Object is an instance of a class. It is a real world entity which holds certain behavior.
# It instantiates the properties and functionalities of the class
s1 = Student("Dibyendu", 10, "Commerce", "10-03-1995")
s1.read()
s1.write()
s1.play()

