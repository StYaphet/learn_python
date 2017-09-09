# 模块json 让你能够将简单的Python数据结构转储到文件中，并在程序再次运行时加载该文件中的数据。
# 你还可以使用json 在Python程序之间分享数据。
# 更重要的是，JSON数据格式并非Python专用的，这让你能够将以JSON格式存储的数据与使用其他编程语言的人分享。
# 这是一种轻便格式，很有用，也易于学习。

# 首先导入模块json，在创建一个数字列表。
import json
numbers = [2, 3, 5, 7, 11, 13]

# 指定了要将该数字存储到其中的文件的名称，通常使用文件扩展.json来指出文件存储的数据为JSON格式。
filename = "numbers.json"
# 接下来，我们以写入模式打开这个文件，让json能够将数据写入其中。
with open(filename, "w") as f_obj:
    # 我们使用json.dump()将数字列表存储到文件numbers.json中
    json.dump(numbers, f_obj)

with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)