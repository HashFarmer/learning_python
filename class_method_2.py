# classmethod的真正用处在于：1、作为factory method，即 alternative constructor
'''
Factory methods are those methods that return a class object (like constructor) for different use cases.
It is similar to function overloading in C++. Since, Python doesn't have anything as such, class methods and static methods are used.
'''


# 也就是说增加了构造函数的适应性，为应对各种可能的情况，见例子如下：
from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

person = Person('Adam', 19)
person.display()

person1 = Person.fromBirthYear('John',  1985)
person1.display()


'''
https://www.programiz.com/python-programming/methods/built-in/classmethod

Here, we have two class instance creator, a constructor and a fromBirthYear method.

The constructor takes normal parameters name and age. 
While, fromBirthYear takes class, name and birthYear, 
calculates the current age by subtracting it with the current year and returns the class instance.

The fromBirthYear method takes Person class (not Person object) as the first parameter cls and 
returns the constructor by calling cls(name, date.today().year - birthYear), 
which is equivalent to Person(name, date.today().year - birthYear)

Before the method, we see @classmethod. 
This is called a decorator for converting fromBirthYear to a class method as classmethod().

'''
