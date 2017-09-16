import re

# 向recompile()传入一个字符串表示正则表达式，它将返回一个Regex模式对象，、
# phone_regex = re.compile("\d\d\d-\d\d\d-\d\d\d")
# # 变量mo是一个通用的名称，用于match对象。
# # 我们在phone_regex上调用search()，向它传入想要超找的字符串，查找的结果保存在变量mo中。
# mo = phone_regex.search("My number is 415-555-4242.")
# print("Phone number found:" + mo.group())

# 在python 中使用正则表达式
# 虽然在 Python 中使用正则表达式有几个步骤，但每一步都相当简单。
# 1.用 import re 导入正则表达式模块。
# 2.用 re.compile()函数创建一个 Regex 对象(记得使用原始字符串)。
# 3.向 Regex 对象的 search()方法传入想查找的字符串。它返回一个 Match 对象。 
# 4.调用 Match 对象的 group()方法，返回实际匹配文本的字符串。

# 利用括号分组
# 添加括号将在正则表达式中创建分组，然后可以使用group()匹配对象方法，从一个分组中获取匹配的文本。
# 第一对括号中是第一组，第二对括号是第二组，向group()传递0或不传入参数，将返回整个匹配的文本。
# 如果想要一次就获取所有的分组，请使用groups()方法
phone_regex = re.compile("(\d\d\d)-(\d\d\d-\d\d\d\d)")
mo = phone_regex.search("My number is 415-555-4242.")
print(mo.group())
print(mo.groups())

# 字符|称为管道。希望匹配许多表达式中的一个时，就可以使用它。要匹配真正的|字符需要进行转义
heroRegex = re.compile(r"Batman|Tina fey")
mo_1 = heroRegex.search("Batman and Tina fey.")
print(mo_1.group())

# 用问号实现可选匹配，字符问号表明它前面的分组在这个模式中是可选的。
bat_regex = re.compile("Bat(wo)?man")
mo_2 = bat_regex.search("The Adventures of Batman")
print(mo_2.group())

mo_3 = bat_regex.search("The Adventure of Batwoman")
print(mo_3.group())

# 用星号匹配零次或多次，要匹配真正的星号，需要对星号进行转义
# 用加号匹配一次或多次，要匹配真正的加号，需要对加号进行转义
# 用花括号匹配特定次数，如果想要一个分组匹配特定次数，就在正则表达式中该分组的后面，跟上花括号包围的数字。
# 除了一个数字还可以指定一个范围，即在花括号中写下一个最小值，一个逗号，一个最大值，可以不写花括号中的第一个或第二个数字，不限定最小值（最小值为0）或最大值

ha_regex = re.compile("(Ha){3}")
mo_4 = ha_regex.search("HaHaHa")
print(mo_4.group())

mo_5 = ha_regex.search("Ha")
print(mo_5 == None)

# python正则表达式默认是“贪心”的，这表示在有二义的情况下，它们会尽可能匹配最长的字符串。
# 花括号的“非贪心”版本匹配尽可能短的字符串，即在结束的花括号中跟着一个问号

greedy_regex = re.compile("(Ha){3,5}")
mo_6 = greedy_regex.search("HaHaHaHaHa")
print(mo_6.group())

non_greedy_regex = re.compile("(Ha){3,5}?")
mo_7 = non_greedy_regex.search("HaHaHaHaHa")
print(mo_7.group())

# search()将返回一个Match对象，包含被查找字符串中“第一次”匹配的文本，而findall()方法将返回一组字符串，包含被查找字符串中的所有匹配。
mo_8 = phone_regex.search("Cell: 415-555-9999 Work: 212-555-0000")
print(mo_8.group())
# findall方法直接返回一个list
mo_9 = phone_regex.findall("Cell: 415-555-9999 Work: 212-555-0000")
print(mo_9)
# 如果正则表达式中有分组，那么findall将返回元组的列表。每个元组表示一个找到的匹配，其中的项就是正则表达式中每个分组的匹配字符串。
# 注意：1. 如果调用在一个没有分组的正则表达式上，方法findall()将返回一个匹配字符串的列表
#      2. 如果调用在一个有分组的正则表达式上，方法findall()将返回一个字符串的元组的列表（每个分组对应一个字符串）

# 点星匹配除换行外的所有字符。
# 通过传入re.DOTALL作为re.compile()的第二个参数，可以让句点字符匹配所有字符，包括换行符。

no_new_line_regex= re.compile(".*")
print(no_new_line_regex.search("Serve the public trust.\nProtect the innocent. \nUphold the law.").group())

new_line_regex = re.compile(".*", re.DOTALL)
print(new_line_regex.search("Serve the public trust.\nProtect the innocent. \nUphold the law.").group())

# 可以向re.compile()传入re.IGNORECASE或者re.I，作为第二个参数。
robocop = re.compile("robocop", re.I)

# 用sub()方法替换字符串
names_regex = re.compile("Agent \w+")
print(names_regex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob."))

# 有时候，你可能需要使用匹配的文本本身，作为替换的一部分。在sub()的第一个参数中，可以输入\1、\2、\3……表示“在替换中输入分组1、2、3……中的文本”
# 但是，通过在字符串的第一个引号之 前加上 r，可以将该字符串标记为原始字符串，它不包括转义字符。
agent_name_regex = re.compile("Agent (\w)\w*")
print(agent_name_regex.sub(r"\1****", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent."))

# 你可以告诉 re.compile()，忽略正则表达式字符 串中的空白符和注释，从而缓解这一点。要实现这种详细模式，可以向 re.compile() 传入变量 re.VERBOSE，作为第二个参数。
# 正则表达式字符串中的注释规则，与普通的 Python 代码一样:#符号和它后面直 到行末的内容，都被忽略。而且，表示正则表达式的多行字符串中，多余的空白字符 也不认为是要匹配的文本模式的一部分。这让你能够组织正则表达式，让它更可读。
phone_regex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)?        # separator
	)''', re.VERBOSE)

# 如果你希望在正则表达式中使用 re.VERBOSE 来编写注释，还希望使用 re.IGNORECASE 来忽略大小写，该怎么办?
# 遗憾的是，re.compile()函数只接受一 个值作为它的第二参数。可以使用管道字符(|)将变量组合起来，从而绕过这个限 制。管道字符在这里称为“按位或”操作符。




































