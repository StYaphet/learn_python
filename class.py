# 1. 创建类
class Dog():
    """一次模拟小狗的简单尝试"""  # 这是一个字符串文档，对这个类的功能做了描述

    def __init__(self, name, age):
        # 类中的函数被称为方法，__init__()是一个特殊的方法，每当根据Dog类创建实例的时候，python都会自动运行它
        # 在这个方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免python默认方法与普通方法发生名称冲突
        # 将__init__()方法定义成包含三个形参，self、name和age。在这个方法的定义中，形参self必不可少，还必须位于其他形参的前面。
        # 因为python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法调用都会自动传递实参self
        # self是一个指向实例本身的引用，让实例能够访问类中的属性和方法。我们不需要传递self，只需传递self之后的形参。
        super(Dog, self).__init__()
        self.name = name
        self.age = age

    def sit(self):  # 也就是说在定义类中的方法时，必须有一个参数，并且第一个参数必须是self
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# 在python 2.7中创建类时，需要做细微的修改——在括号内包含单词object：
# class ClassName(object):
    # --snip--

# 2.根据类创建实例
my_dog = Dog("willie", 6)
your_dog = Dog("lucy", 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + my_dog.name.title() + ".")
print("Your dog is " + str(my_dog.age) + " years old.")
your_dog.sit()

# 要访问实例的属性，可以使用句点表示法。
# my_dog.name
# 在Dog类中引用这个属性时，使用的是self.name
# 根据Dog类创建实例后，就可以使用句点表示法来调用Dog类中定义的任何方法。
my_dog.sit()
my_dog.roll_over()

# 3.给属性指定默认值


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        super(Car, self).__init__()
        self.make = make
        self.model = model
        self.year = year
        # 这里通过在__init__()创建新实例时，创建一个名为odometer_reading的属性，并将其初始值设为0
        # 来给属性指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_new_car = Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 4.修改属性的值
# 1.直接修改，修改属性值最简单的方式就是通过实例直接方位它。
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 2.通过方法修改属性的值，可以创建一个更新属性的方法，这样就可以无需直接访问属性，而将值传递给一个方法，有它在内部进行更新
my_new_car.update_odometer(25)
my_new_car.read_odometer()
# 可对方法update_odometer()进行扩展，使其在修改里程表读数时做额外的工作。下面来添加一些逻辑，禁止任何人将里程表读数往回调
# 3.通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


class Battery():

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

# 5.继承
# 创建子类时，父类必须包含在当前文件中，且位于子类前面。定义子类时，必须在括号内指定父类的名称。
# 方法__init__()接受创建Car实例所需的信息


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)  
        # super()是一个特殊函数，帮助python将父类和子类关联起来
        # 这行代码让python调用 ElectricCar 的父类的 __init__()，让 ElectricCar 实例包含父类所有属性
        # 父类也被称为超类
        # 给子类定义属性
        self.battery = Battery()
    # # 给子类定义方法
    # def describe_battery(self):
    # 	"""打印一条描述电瓶容量的消息"""
    # 	print("This car has a " + str(self.battery_size) + "-kWh battery.")
    # 重写父类的方法

my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
