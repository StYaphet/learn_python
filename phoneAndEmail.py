#! python3 

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?          	# area code
    (\s|-|\.)?                  	# separator
    (\d{3})		 					# first 3 digits
	(\s|-|\.)						# separator
	(\d{4})							# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
	)''', re.VERBOSE)


emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+ 				# username 
	@ 								#@symbol
	[a-zA-Z0-9.-]+ 					# domain name
	(\.[a-zA-Z]{2,4}) 			# dot-something 
	)''', re.VERBOSE)

# pyperclip.paste()函数将取得一个 字符串，内容是剪贴板上的文本，findall()正则表达式方法将返回一个元组的列表。

text = str(pyperclip.paste())
matches = []
# 因为
for group in phoneRegex.findall(text):
	phoneNum = "-".join([group[1], group[3], group[5]])
	if group[8] != "":
		phoneNum += " x" + group[8]
	matches.append(phoneNum)
for group in emailRegex.findall(text):
	matches.append(group[0])



if len(matches) > 0:
	pyperclip.copy("\n".join(matches))
	print("Copied to clipboard:")
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


# haoyipen@bytedance.com ;aklsdjfa;k sdjfoiwquer afdsjjk a;sldk