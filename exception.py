# print(5 / 0)
# ZeroDivisionError是一个异常对象。当python无法按照你的要求做的时候，就会创建这样的对象
# 在这种情况下，python将会停止运行程序，并指出发生了哪些异常，饿哦们就可以根据这些信息对程序进行修改

# 当认为可能发生了错误时，可编写一个try-except代码块来处理可能引发的异常。

try:
    print(5 / 0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# 如果try-except 代码块后面还有其他代码，程序将接着运行，因为已经告诉了Python如何处理这种错误

# 1.使用异常避免崩溃
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == "q":
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

# 2.处理FileNotFoundError异常

# filename = "alice.txt"
# try:
#     with open(filename) as file_object:
#         content = file_object.read()
# except FileNotFoundError:
#     msg = "Sorry, the file " + filename + " does not exist."
#     print(msg)

filename = "alice.py"

try:
    with open(filename) as f_obj:
        content = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)
else:
    words = content.split()
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")


# 1.使用多个文件
