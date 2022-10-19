
class Dog:

    species = "dog"


    # 不带@classmethod, 不带@staticmethod，不带self，可以用类名.操作
    # 带self，则无法用类名.操作
    def bark(self):
        print("Barking dog...")
        self.eat()


    # 不带@classmethod, 不带@staticmethod，不带self，可以用类名.操作
    def add(x, y):
        print(x + y)

    
    #staticmethod调用不了实例属性和方法
    @staticmethod
    def run():
        print("Running dog...")
        Dog.species = "doogoo" #staticmethod也可以操作修改类属性
        # self.bark() #NameError: name 'self' is not defined

    def eat(self):
        print("Eating dog...")
        
        

# 1:
# 说明staticmethod有两种调用方式
# Dog.run()
d = Dog()
d.run()

# 2:
# 说明类属性有两种方法方式
# print(Dog.species)
# print(d.species)


#d = Dog()                # 3:
#d.add(1,2)              #TypeError: Dog.add() takes 2 positional arguments but 3 were given，说明add不是实例方法
#Dog.add(1, 2)


