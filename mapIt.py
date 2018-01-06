#! /usr/local/bin/python3
# 然后，更改.py 文件 的权限，运行 chmod +x pythonScript.py，使之成为可执行文件。
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

# 导入webbrowser模块，用于加载浏览器；导入sys模块，用于读入可能的命令行参数。
import webbrowser, sys, pyperclip
# sys.argv标量保存了程序的文件名和命令行参数的列表。如果这个列表中不只有文件名，那么其长度的返回值就会大于1，这就意味着提供了命令行参数
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])
    print(address)
else:
	# TODO: Get address from clipboard.
	address = pyperclip.paste()
	print(address)
webbrowser.open("https://www.google.com/maps/place/" + address)
