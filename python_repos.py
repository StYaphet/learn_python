# 导入模块requests
import requests
# 导入pygal以及要应用于图表的pygal样式
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
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
names, stars = [], []

# 获取数据
for repo_dict in repo_dicts:
	names.append(repo_dict["name"])
	stars.append(repo_dict["stargazers_count"])

# 可视化
# 使用LightenStyle类(别名LS)定义了一种样式，并将其基色设置为深蓝色
# 我们还传递了实参base_style，以使用LightColorizedStyle类(别名LCS)
mystyle = LS("#333366", base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
# 我们使用Bar() 创建一个简单的条形图，并向它传递了my_style 
# 还传递了另外两个样式实参:让标签绕  轴旋转45度 (x_label_rotation=45 )，并隐藏了图例(show_legend=False )
chart = pygal.Bar(my_config, style=mystyle)
chart.title = "Most-Starred Objective-C Projects on GitHub"
# 将属性x_labels 设置为列表names 。
chart.x_labels = names
# 由于我们不需要给这个数据系列添加标签，因此在此处添加数据时，将标签设置成了空字符串。
chart.add("", stars)
chart.render_to_file("python_repos.svg")





