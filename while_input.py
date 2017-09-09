# message = input("Tell me something, and I will repeat it back to you: ")
# print(message)
# # 函数input() 接受一个参数:即要向用户显示的提示 或说明，让用户知道该如何做。

# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name?\n"

# name = input(prompt)
# print("\nHello, " + name + "!")

# age = input("How old are you?")
# age = int(age)
# if age > 18:
# 	print ("You are an adult!")

# current_number = 1
# while current_number < 5:
# 	print(current_number)
# 	current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
# 	message = input(prompt) 
# 	if message != "quit":
# 		print(message)

# prompt = "\nTell me something, and I will repeat it back to you:" 
# prompt += "\nEnter 'quit' to end the program. "
# active = True 
# while active:
# 	message = input(prompt)
# 	if message == 'quit': 
# 		active = False
# 	else: 
# 		print(message)

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
# while unconfirmed_users:
# 	confirmed_user = unconfirmed_users.pop()
# 	print("Verifying user: " + current_user.title())
# 	confirmed_users.append(confirmed_user)
# print("\nThe following users have been confirmed:") 
# for confirmed_user in confirmed_users:
# 	print(confirmed_user.title())

responses = {}
is_active = True
while is_active:
	name = input("\nWhat is your name? ")
	response = input("Which mountain would you like to climb someday? ")
	responses[name] = response
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat == "no":
		is_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")















