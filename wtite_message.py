filename = "programming.txt"
# 1.写入空文件
with open(filename, "w") as file_object:
    file_object.write("I love programming.")

# 在这个示例中，调用open()时提供了两个实参。第一个实参也是要打开的文件的名称；
# 第二个实参("w")告诉python，我们要以写入模式打开这个文件。
# 打开文件时，可以指定 读取模式("r")，写入模式("w")，附加模式("a")或让你能够读取和写入文件的模式("r+")
# 如果省略了模式实参，python将以默认的只读形式打开文件。
# 如果你要写入的文件不存在，函数open()将自动创建它。
# 然而，以写入("w")模式打开文件时要千万消息，如果指定的文件已经存在，python将在返回文件对象前清空该文件。
# 注意python只能将字符串写入文本文件。要将数值存储到文本文件中，必须先使用函数str()将其转换为字符串格式

# 2.写入多行，使用\n进行换行
with open(filename, "w") as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

# 3.附加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
