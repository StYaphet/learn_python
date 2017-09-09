def greet_user(user_name):
	"""显示简单的问候语"""
	print("Hello, " + user_name.title() + "!")

greet_user("dashuaige")

# 请注意，在这个函数的定义中，修改了形参的排列顺序。
# 由于给animal_type 指定了默认值，无需通过实参来指定动物类型，
# 因此在函数调用中只包含一个实参——宠物的名字。
# 然而，Python依然将这个实参视为位置实参，
# 因此如果函数调用中只包含宠物的名字，
# 这个实参将关联到函数定义中的第一个形参。
# 这就是需要将pet_name 放在形参列表开头的原因所在。
# 在任何情况下都必须给pet_name 提供实参
# 指定该实参时可以使用位置方式，也可以使用关键字方式。

def describe_pet(pet_name,animal_type = "dog"):
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

describe_pet(animal_type='hamster', pet_name='harry')

describe_pet("cat")

def get_formatted_name(first_name, last_name, middle_name = ""):
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name("jimi", "hendirix")
print(musician)

musician = get_formatted_name("jomi", "hendirix", "lee")
print(musician)

def build_person(first_name, last_name):
	person = {"first_name" : first_name, "last_name" : last_name}
	return person

musician = build_person("jimi", "hedrix")
print(musician)

def greet_users(names): 
	for name in names:
		msg = "Hello, " + name.title() + "!" 
		print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	completed_models.append(current_design)

print("\nThe following models have been printed:") 
for completed_model in completed_models:
	print(completed_model)

def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
completed_models = []
print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)



# 要将列表的副本传递给函数，可以像下面这样做,切片表示法[:]创建列表的副本
# function_name(list_name[:])

print_models(unprinted_designs[:],completed_models)


def make_pizza(*toppings): # 形参名*toppings中的星号让python创建一个名为toppings的空数组，并将收到的所有值都封装到这个元组中
						   # 注意：python将实参封装到一个元组中，即便函数只收到一个值也是如此
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza("pepperoni")
make_pizza("mushrooms","green peppers","extra cheese")


# 如果要让函数接受不同类型的实参，
# 必须在函数定义中将接纳任意数量实参的形参放在最后。
# Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。

def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza(14, "pepperoni")
make_pizza(12, "mushrooms","green peppers","extra cheese")


# 形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典，
# 并将收到的所有名称—值对都封装到这个字典中。

def build_profile(first, last, **user_info):
	profile = {}
	profile["first_name"] = first
	profile["last_name"] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile("albert", "einstein", location = "princeton", field = "physics")
print(user_profile)


























































