
class ExampleClass(object):
  class_attr = 0

  def __init__(self, instance_attr):
    self.instance_attr = instance_attr
    self.class_attr = 1 ## 问题出在这里，相当于为foo对象添加了名为class_attr的实例属性，碰巧与类属性同名而已

if __name__ == '__main__':
    foo = ExampleClass(1)
    bar = ExampleClass(2)

    #print the class attribute as a porperty of a foo
    print(foo.class_attr)
    print(foo.__class__.class_attr)


    
    #modify the class attribute as a foo property
    foo.class_attr = 5  # 问题出在这里，相当于为foo对象添加了名为class_attr的实例属性，碰巧与类属性同名而已
    print(foo.class_attr)
    #5

    # 对“实例”来说，“类属性”只能被读，而不能被修改，一修改，就是实例属性了，而类属性依然不变
    #print the class attribute as a porperty of a bar
    print(bar.class_attr)  # 说明实例修改不了类属性的值
    # 0 
    #oups !!!!

    ExampleClass.class_attr = 999
    print(foo.class_attr)  # 0 !!! 这种形式首先获取的是 "实例属性"
    print(foo.__class__.class_attr)
    print(bar.class_attr)
