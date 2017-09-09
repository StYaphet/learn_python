# 1.读取文件
with open("pi_digits.txt") as file_object:
    content = file_object.read()
    print(content)
# 在这个程序中，第一行代码做了大量的工作。
# open()函数：
#     要以任何方式使用文件——哪怕仅仅是打印其内容，都得先 打开 文件，这样才能访问它。
#     函数open()接受一个参数：将要打开的文件的名称。python在当前执行的文件所在的目录中查找指定的文件。
#     函数open()返回一个表示文件的对象。在这里，open("pi_digits.txt")返回一个表示文件pi_digits.txt的对象
#     python将这个对象储存在我们将在后面使用的变量中。
# 关键字 with：
#     关键字 with 在不需要访问文件后将其关闭。在这个程序中，注意到我们调用了open()，但没有调用close()
#     你也可以使用 open() 和 close() 来打开和关闭文件，但是这样做时，如果程序存在bug，导致close()语句未执行
#     文件将不会关闭，未妥善的关闭文件可能导致数据丢失或者受损。如果在程序中过早的调用close()
#     你会发现需要文件时它已经关闭，无法访问。
# read():
#     有了表示文件的对象后，我们使用方法read()读取这个文件的全部内容，并将其作为一个常常的字符串储存在变量content中
#     这样通过打印content的值，我们就可以将这个文本文件的全部内容显示出来
#     相比原始文件，该输出唯一不同的地方是末尾多了一个空行，要删除多出来的空行，可在print语句中使用rstrip()

# 当将 pi_digits.txt这样的简单文件名传递给函数open()时，python将在当前执行的文件所在的目录中查找文件。
# 要让python打开不与程序文件位于同一个目录中的文件，需要提供文件路径，它让python到系统的特定位置去查找。
# 可提供相对路径或者绝对路径，绝对路径通常比相对路径更长，因此将其储存在一个变量中，再将该变量传递给open()会有帮助

file_path = "/Users/ShorewB/Python开发/learn_python/pi_digits.txt"
with open(file_path) as file_object:
    content = file_object.read()
    print(content)

# 2.逐行读取
file_name = "pi_digits.txt"
with open(file_name) as file_object:  # 调用open() 后，将一个表示文件及其内容的对象存储到了变量file_object 中
    for line in file_object:
        print(line.rstrip())
# 3.创建一个包含文件各行内容的列表
file_name = "pi_digits.txt"
with open(file_name) as file_object:  # 使用关键字with 时，open() 返回的文件对象只在with代码块内可用
    lines = file_object.readlines()  # 如果要在with 代码块外访问文件的内容，
    # 可在with代码块内将文件的各行存储在一个列表中，并在with 代码块外使用该列表
    # readlines()从文件中读取每一行，并将其存储在一个列表中

for line in lines:
    print(line.rstrip())

# 4.使用文件的内容
pi_string = ""
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

# 注意读取文件时，python将其中的所有文本都解读为字符串。
# 如果你读取的是数组，并要将其作为数值使用，就必须使用int()将其转换为整数，或者使用float()将其转换为浮点数

# 5.包含一百万位的大型文件
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

print(pi_string[:52] + "...")
print(len(pi_string))
