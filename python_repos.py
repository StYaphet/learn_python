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

print(response_dict.keys())