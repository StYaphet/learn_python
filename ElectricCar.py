from Car import Car


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
