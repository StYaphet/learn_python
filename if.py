cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else :
		print(car.title())

# Python的真假值分别为Ture与False
# 函数lower() 不会修改存储在变量中的值

requested_topping = 'mushrooms'
if requested_topping != 'anchovies': 
	print("Hold the anchovies!")

answer = 17
if answer != 42:
	print("That is not the correct answer. Please try again!")

# and 相当于&&, or相当于 ||

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if "mushrooms" in requested_toppings:
	print("mushroom !!!")

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

age = 19
if age > 18:
	print("You are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please register to vote as soon as you turn 18!")

age = 12
price = 0
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10

print("Your admission cost is $" + str(price) + ".")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")







