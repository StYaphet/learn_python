import re

# 向recompile()传入一个字符串表示正则表达式，它将返回一个Regex模式对象，、
phone_regex = re.compile("\d\d\d-\d\d\d-\d\d\d")
# 变量mo是一个通用的名称，用于match对象。
# 我们在phone_regex上调用search()，向它传入想要超找的字符串，查找的结果保存在变量mo中。
mo = phone_regex.search("My number is 415-555-4242.")
print("Phone number found:" + mo.group())