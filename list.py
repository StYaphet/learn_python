#1. 访问列表元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
print (bicycles[0])
print (bicycles[0].title())
print (bicycles[-1])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

#2. 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)
motorcycles[0] = "ducati"
motorcycles[0] = "honda"
print (motorcycles)
motorcycles.append("ducati")
print (motorcycles)

motorcycles = []
print (motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0, "ducati")
print(motorcycles)
del(motorcycles[0])
print(motorcycles)
del(motorcycles[1])
print(motorcycles)
motorcycles.insert(1, "yamaha")
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(popped_motorcycle)
print("The last motorcycle I owned was a " + popped_motorcycle.title() + ".")
first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove("honda")
print(motorcycles)
motorcycles.insert(0, "honda")
print(motorcycles)

#3. 组织列表
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)
print(len(cars))

#4. 操作列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print (magician)

for magician in magicians:
	print (magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick, " + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

for value in range(1,10): #range,包括start不包括end
	print(value)

number = list(range(1,20,3))
print(number)

squares = []
for number in range(1,11):
	square = number ** 2;
	squares.append(square)
	print(squares)

digital = list(range(1,11))
print(min(digital))
print(max(digital))
print(sum(digital))

#5. 列表解析
squares = [value ** 2 for value in range(1,11)]
print(squares)

divide_by_3 = [value * 3 for value in range(1,11)]
print(divide_by_3)

cubes = [value ** 3 for value in range(1,11)]
print(cubes)

#6. 列表切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3]) #切片指明范围的时候用的是[],同时包含startIndex而不包含endIndex

	#提取第二个到第四个元素,因为包含startIndex而不包含endIndex,所以起始index应该是1,终止index应该是3+1
print(players[1:4])
print(players[:4])
print(players[1:])
	#负数索引返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任何切片。
print(players[-3:])
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player)

#7. 复制列表:要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引([:] )
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:] #会生成一个新的列表

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)






