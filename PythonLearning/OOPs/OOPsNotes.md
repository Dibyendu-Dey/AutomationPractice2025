OOPs: OOP stands for Object-Oriented Programming. 
      It is a programming that takes care of secure data.

Class: Class is a blueprint that contains group of functions and data members inside a single entity.

Self: Self keyword is a default parameter that holds the address or the value of the data members or parameters passed 
      to the methods.

syntax: is a way of writing code or the rules for writing a block of code.

Data Members: Data members refers to the variables or attributes that hold the data or state of an instance of the class.
              These variables are associated with the object of the class and represent the properties of the class

Example:
class: Vehicle
Data Members: Mileage, Engine, fuel_type, model, year
Function: race, brake, honk, display_info

Init method (__init__) or Constructor is used to assign the values to a data members of a class when an object of the
class is created.

Inheritance: Inheritance is a capability of a class to acquire the properties of the parent class.
There are 5 types of inheritance:
1. single inheritance: 1 Parent and 1 Child
2. multiple inheritance: Multiple Parent and 1 Child
3. multilevel inheritance: GrandParent, Parent and Child
4. hierarchical inheritance: 1 Parent and Multiple Child
5. hybrid inheritance: Combination of more than 2 inheritance.

Polymorphism: poly means many and morphism means forms. So as the name suggest a particular object or thing can have
many forms. There are two types of Polymorphisms:
1. Function or Method Overloading: Where the function/method name will be same but the task performed will be different.
   def func1(a,b):
        return a + b
   def func1(c, d, e):
       return c * d - e
2. Function or Method Overriding: Where the function/method name, arguments names and no. of arguments will be same but 
   task performed will be different.
    def func1(a,b):
        return a + b
   def func1(a, b):
       return a + b 
