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
