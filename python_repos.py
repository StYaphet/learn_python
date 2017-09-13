# 导入模块requests
import requests
# 储存API调用的URL
url = "https://api.github.com/search/repositories?q=language:objective-c&sort=stars"
# 然后使用requests来执行，我们调用get()并将URL传递给它，再将响应对象存储在变量r中
# 响应对象包含一个名为status_code的属性，它让我们知道请求是否成功了
r = requests.get(url)
print("Status code:", r.status_code)

# 将API响应存储在一个变量中，因为这个api返回json格式的信息，因此我们使用方法json()将这些信息转为一个python字典
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])
# 打印了与'total_count' 相关联的值，它指出了GitHub总共包含多少个Objective-C仓库。
repo_dicts = response_dict["items"]
print("Repositories returned:", len(repo_dicts)) 

# 提取了repo_dicts 中的第一个字典，并将其存储在repo_dict 中
repo_dict = repo_dicts[0]
# 接下来，我们打印这个字典包含的键数，看看其中有多少信息
print("\nKeys:",len(repo_dict))

# 答应这个字典的所有键，看看其中包含了哪些信息
# for key in sorted(repo_dict.keys()):
# 	print(key)

for repo_dict in repo_dicts:
	print("\nSelected information about first repository:") 
	print('Name:', repo_dict['name'])
	print('Owner:', repo_dict['owner']['login'])
	print('Stars:', repo_dict['stargazers_count'])
	print('Repository:', repo_dict['html_url']) 
	print('Created:', repo_dict['created_at']) 
	print('Updated:', repo_dict['updated_at'])
	print('Description:', repo_dict['description'])









