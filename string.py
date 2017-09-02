#1. 改变字符串中字母的大小写
name = "i am captain america"
print (name.title())
print (name.upper())
print (name.lower())

#2. 合并(拼接)字符串
first_name = "captain"
last_name = "america"
full_name = first_name + " " + last_name
print (full_name)
print ("Hello, " + full_name.title() + "!")
message = "Hello, " + full_name.title() + "!"
print (message)

#3. 使用制表符或换行符来添加空白
print ("Python")
print ("\tPython")
print ("language: \n\tObjective-C\n\tJavascript\n\tPython")

#4. 删除空白
favorite_language = "Python "
print (favorite_language)
print (favorite_language.rstrip())
favorite_language = favorite_language.rstrip()
print (favorite_language)
favorite_language = " Python "
print (favorite_language.rstrip())
print (favorite_language.lstrip())
print (favorite_language.strip())

#5. 使用字符串时避免语法错误
message = "One of Python's strengths is its diverse community."
print (message)
message = 'One of Python\'s strengths is its diverse community.'
print (message)












