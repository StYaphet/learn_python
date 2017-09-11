from die import Die
import pygal

die = Die()

results = []
for roll_num in range(1000):
	result = die.roll()
	results.append(result)

# print(results)

frequencies = []
for value in range(1, die.num_sides+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# print(frequencies)
# 对数据结果进行可视化，为了创建条形图，我们创建了一个pygal.Bar()实例，并将其储存在hist中。
hist = pygal.Bar()
# 接下来，设置hist的属性title，将掷D6骰子的可能结果用作x轴的标签，并给每个轴都添加了标题
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [1, 2, 3, 4, 5, 6]
hist.x_title = "Result" 
hist.y_title = "Frequency of Result"
# 使用add()将一系列值添加到图表中（向它传递要给添加的值指定的标签，还有一个列表，其中包含了将要出现在图标中的值）
hist.add("D6", frequencies)
# 最后我们将这个图标渲染成为一个svg文件，这种文件的扩展名必须为.svg
hist.render_to_file("die_visual.svg")



