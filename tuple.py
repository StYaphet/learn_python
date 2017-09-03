# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。
# 元组看起来犹如列表，但使用圆括号而不是方括号来标识。
dimensions = (200, 50)
print(dimensions[1])
print(dimensions[0])
# dimensions[0] = 22   #错误，元组中的数据不能被修改
for dimension in dimensions:
	print(dimension)
# 虽然不能修改元组的元素，但可以给存储元组的变量赋值。
dimensions = (200, 50) 
print("Original dimensions:") 
for dimension in dimensions:
	print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions: 
	print(dimension)














