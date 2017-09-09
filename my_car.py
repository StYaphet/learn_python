# from Car import Car
import ElectricCar
import Car
# from Car import *
# 不推荐使用这种导入方式
# 需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法来方位类
# import 语句让python打开模块Car，并导入其中的Car类，这样我们就可以使用Car类了，就像它是在这个文件中定义的一样

from collections import OrderedDict

my_new_car = Car.Car("audi", "a4", 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar.ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

# OrderedDict 类兼具列表和字典的主要优点（在将信息关联起来的同时保留原来的顺序）
favorite_languages = OrderedDict()
favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

# python的编码风格：类名采用驼峰命名法，每个单词的首字母都大写，而且不适用下划线。
# 实例名和模块名都是用小写格式，并在单词之间加上下划线
# 对于每个类都应紧跟在类定义后面包含一个文档字符串，这个字符串简要的描述类的功能
# 每个模块也应该包含一个文档字符串，对其中的类可以用于做什么进行描述
# 需要同时引入标准库中的模块和你写的模块时，先编写导入标准库模块的import语句，再添加一个空行
# 然后编写导入你自己编写的模块的import语句
# 在包含许多条import语句的程序中，这种做法更容易让人明白程序使用的各个模块都来自何方
