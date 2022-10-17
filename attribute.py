class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    def foo():
        legs = 2 #局域变量

    def bar(self):
        self.bar = 1

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

blu.species = "flying bird"  # 类外获得一个与class attribute同名的instance attribute

# access the class attributes
print("Blu is a {}".format(blu.species)) # 说明先从instance attribute里面找这个attribute名，再从class attribute里找这个attribute名
print("Blu is a {}".format(blu.__class__.species))

print("Woo is also a {}".format(woo.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format( blu.name, blu.age))
print("{} is {} years old".format( woo.name, woo.age))

# print(woo.legs)

print("bbb".format(blu.bar)) # 为什么这个输不出来？
print(woo.bar)
