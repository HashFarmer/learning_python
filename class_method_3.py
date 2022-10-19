# factory method 的继承，不乱，自适应
'''
Whenever you derive a class from implementing a factory method as a class method, it ensures correct instance creation of the derived class.

You can create a static method for the above example but the object it creates, will always be hard coded as Base class.

But, when you use a class method, it creates the correct instance of the derived class.
'''


from datetime import date

# random Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #静态方法也可以做 factory method，但是在继承类中会出问题,即 写死了 Person
    @staticmethod
    def fromFathersAge(name, fatherAge, fatherPersonAgeDiff):
        return Person(name, date.today().year - fatherAge + fatherPersonAgeDiff)


    #类方法可以避免, cls 可以自动变化适应
    @classmethod
    def fromBirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

class Man(Person):
    sex = 'Male'


man = Man.fromBirthYear('John', 1985)
print(isinstance(man, Man))

man1 = Man.fromFathersAge('John', 1965, 20)
print(isinstance(man1, Man))



'''
Here, using a static method to create a class instance wants us to hardcode the instance type during creation.
This clearly causes a problem when inheriting Person to Man.
fromFathersAge method doesn't return a Man object but its base class Person's object.
This violates the OOP paradigm. 
Using a class method as fromBirthYear can ensure the OOP-ness of the code 
since it takes the first parameter as the class itself and calls its factory method.

'''
