
class ExampleClass(object):
  class_attr = 0

  def __init__(self, instance_attr):
    self.instance_attr = instance_attr

if __name__ == '__main__':
    foo = ExampleClass(1)
    bar = ExampleClass(2)

    #print the class attribute as a porperty of a foo
    print(foo.class_attr)
    #0


    #modify the class attribute as a foo property
    foo.class_attr = 5  # 问题出在这里，相当于为foo对象添加了名为class_attr的实例属性，碰巧与类属性同名而已
    print(foo.class_attr)
    #5


    #print the class attribute as a porperty of a bar
    print(bar.class_attr)  # 说明实例修改不了类属性的值
    # 0 
    #oups !!!!

    ExampleClass.class_attr = 999
    print(foo.class_attr)  # 0 !!! 这种形式首先获取的是 "实例属性"
    print(foo.__class__.class_attr)
    print(bar.class_attr)