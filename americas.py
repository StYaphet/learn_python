import pygal.maps.world 

# 创建一个Worldmap实例，并设置该地图的title属性
wm = pygal.maps.world.World()
wm.title = 'North, Central, and South America'
# 使用了方法add()，它接受一个标签和一个列表，其中后者包含我们要突出的国家的国别码。
# 每次调用add()都将为指定的国家选择一种新颜色，并在图标左边显示该颜色和指定的标签
wm.add("North America", {"ca" : 34126000, "us" : 309349000, "mx" : 113423000})

wm.render_to_file('na_populations.svg')