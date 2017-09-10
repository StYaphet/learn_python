# 要为函数编写测试用例，可先导入模块unittest以及要测试的函数，
# 再创建一个继承unittest.TestCase 的类，并编写一系列方法对函数行为的不同方面进行测试。

import unittest
from name_function import get_formatted_name

# 首先创建一个NameTestCase的类，用于包含一系列针对get_formatted_name()的单元测试
# 可以随便给这个类命名，但最好让它看起来与要测试的函数相关，并包含字样Test。
# 这个类必须继承unittest.TestCase类，这样Python才知道如何运行你编写的测试。
class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    # 运行testname_function.py时，所有test开头的方法都将自动运行
    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗?"""
        formatted_name = get_formatted_name("janis", "joplin")
        # 在这里我们使用了unittest类最有用的功能之一：一个断言方法，、
        self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()
