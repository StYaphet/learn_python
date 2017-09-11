from die import Die
import pygal

die_1 = Die()
die_2 = Die(10)

results = []
for roll_num in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# print(results)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)
# 对数据结果进行可视化，为了创建条形图，我们创建了一个pygal.Bar()实例，并将其储存在hist中。
hist = pygal.Bar()
# 接下来，设置hist的属性title，将掷D6骰子的可能结果用作x轴的标签，并给每个轴都添加了标题
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = list(range(2,17))
hist.x_title = "Result" 
hist.y_title = "Frequency of Result"
# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含了将要出现在图标中的值）
hist.add("D6 + D10", frequencies)
# 最后我们将这个图标渲染成为一个svg文件，这种文件的扩展名必须为.svg
hist.render_to_file("die_visual.svg")



