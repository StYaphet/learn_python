# 1.第一种导入方法：只需编写一条import语句并在其中指定模块名，就可以在程序中使用该模块中的所有函数

import pizza # python读取这个文件时，这一行让python打开文件pizza.py，并将其中的所有函数都复制到这个程序中。
			 # 我们是看不到复制的代码的，因为这个程序运行时，python在幕后复制这些代码，只需知道在本程序中可以使用pizza.py中定义的所有函数

# 要调用被导入模块中的函数，可指定导入的模块的名称pizza和函数名make_pizza()，并用句点分隔它们

pizza.make_pizza(14, "pepperoni")
pizza.make_pizza(12, "mushroom", "green peppers", "extra cheese")


# 2.还可以导入模块中的特定函数，这种导入方法的语法如下：
# from module_name import function_name
# 通过逗号分隔函数名，可根据需要从模块中导入任意数量的函数:
# from module_name import function_0, function_1, function_2

from pizza import make_pizza
#若使用这种语法，调用函数时就无需使用句点。由于我们在import语句中显示的导入了函数make_pizza()，因此调用它时只需指定其名称


# 3.使用 as 给函数指定别名,如果要导入的函数名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名——函数的另一个名称，相当于一个外号
# 要给函数指定这种特殊外号，需要在导入它时这么做
# 下面给函数make_pizza()指定了别名mp()。这是在 import 语句中使用 make_pizza as mp 来实现的，关键字 as 将函数重命名为你提供的别名

from pizza import make_pizza as mp


# 4.使用 as 给模块指定别名
# 你还可以给模块指定别名。通过给模块指定简短的别名，让你能够更轻松的调用模块中的函数，这样在调用模块中的函数时句点前边只需写你设置的模块别名就可以
# 通用语法如下：
# import module_name as mn

import pizza as pizza

# 5.导入模块中的所有函数
# 使用星号运算符可让python导入模块中的所有函数
# 通用语法：
# from module_name import *

from pizza import *






















