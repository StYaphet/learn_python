import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

# 定义了一个名为plot_dicts的列表，其中包含三个字典，分别针对HTTPie、Django和Flask
# 每个字典中都包含两个键:"value"和"label"。
# pygal根据与键value相关联的数字来确定条形的高度，并使用与"label"相关联的字符串给条形创建工具提示
plot_dicts = [
	{"value":16101, "label" : "Description of httpie."},
	{"value":15028, "label" : "Description of django."},
	{"value":14798, "label" : "Description of flask."},
	]	

chart.add("", plot_dicts)
chart.render_to_file("bar_descriptions.svg")