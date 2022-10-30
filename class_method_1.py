
# classmethod的真正用处不在于修改类变量，这一点staticmethod可以做到，实例函数也可以做到


class Person:
    age = 25

    @classmethod
    def printAge(cls):
        print('The age is:', cls.age)

# create printAge class method
# Person.printAge = classmethod(Person.printAge) # 等价于@classmethod, 两者选其一

# 1:
# classmethod有两种调用方式
Person.printAge()

# 2:
p1 = Person()
p1.printAge()
