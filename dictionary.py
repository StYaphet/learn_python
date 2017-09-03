#1. 字典的基本使用
alien_0 = {"color":"green","point":5}
alien_0 = {"color":"green",}
print(alien_0["color"])
alien_0 = {"color":"green","point":5}
new_point = alien_0["point"]
print("You just earned " + str(new_point) + " points!")
print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green' 
alien_0['points'] = 5
print(alien_0)

print("The alien is " + alien_0['color'] + ".")
alien_0["color"] = 'yellow'
print("The alien is " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))
if alien_0["speed"] == "slow":
	x_increment = 1
elif alien_0["speed"] == "medium":
	x_increment = 2
else: 
	x_increment = 3

alien_0["x_position"] += x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0 = {'color': 'green', 'points': 5}
del(alien_0["points"])
print(alien_0)

#字典的书写格式
favorite_languages = {
	'jen': 'python', 
	'sarah': 'c', 
	'edward': 'ruby', 
	'phil': 'python', 
	}

# 如何将较长的print语句分成多行。
# 单词print 比大多数字典名都短，
# 因此让输出的第一部分紧跟在左括号后面是合理的。
# 请选择在合适的地方拆分要打印的内容
# 并在第一行末尾加上一个拼接运算符(+ )。
# 按回车键进入print 语句的后续各行，
# 并使用Tab键将它们对齐并缩进一级。
# 指定要打印的所有内容后，
# 在print 语句的最后一行末尾加上右括号。
print("Sarah's favorite language is " + 
	favorite_languages['sarah'].title() + 
	".")

#2. 遍历字典
user_0 = {
	'username': 'efermi', 
	'first': 'enrico', 
	'last': 'fermi',
	}
# 方法items() 返回一个键—值对列表。
for key,value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title())

# 方法keys() 并非只能用于遍历;实际上，它返回一个列表，其中包含字典中的所有键
for name in favorite_languages.keys():
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print("Hi " + name.title() +
			", I see your favorite language is " + 
			favorite_languages[name].title() + "!"
			)

# 按顺序遍历字典中的所有键,可使用函数sorted() 来获得按特定顺序排列的键列表的副本
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")

# 方法values() ，它返回一个值列表，而不包含任何键。
print("The following languages have been mentioned:") 
for language in favorite_languages.values():
	print(language.title())

for language in set(favorite_languages.values()):
	print(language.title())


alien_0 = {'color': 'green', 'points': 5} 
alien_1 = {'color': 'yellow', 'points': 10} 
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens: 
	print(alien)

aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow' 
		alien['speed'] = 'medium' 
		alien['Zpoints'] = 10

for alien in aliens[0:5]:
	print(alien) 
print("...")

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms',
		'extra cheese'
		], 
}

print("You ordered a " + 
	pizza['crust'] + 
	"-crust pizza " +
	"with the following toppings:")
for topping in pizza["toppings"]:
	print("\t" + topping)


favorite_languages = {
	'jen': [
		'python', 
		'ruby'], 
	'sarah': ['c'],
	'edward': [
		'ruby', 
		'go'], 
	'phil': [
		'python', 
		'haskell'
		], 
	}

for name,languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())


users = { 
	'aeinstein': {
		'first': 'albert', 
		'last': 'einstein', 
		'location': 'princeton', 
		},
	'mcurie': {
		'first': 'marie', 
		'last': 'curie', 
		'location': 'paris', 
		},
}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last'] 
	location = user_info['location']
	print("\tFull name: " + full_name.title()) 
	print("\tLocation: " + location.title())






























