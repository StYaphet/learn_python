import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5] 
# y_values = [1, 4, 9, 16, 25]

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# 要删除数据 点的轮廓，可在调用scatter() 时传递实参edgecolor='none'
# 要修改数据点的颜色，可向scatter() 传递参数c ，并将其设置为要使用的颜色的名称
# 颜色映射 (colormap)是一系列颜色，它们从起始颜色渐变到结束颜色。
# 要使用这些颜色映射，你需要告诉pyplot 该如何设置数据集中每个点的颜色。
# 我们将参数c 设置成了一个y值列表，并使用参数cmap 告诉pyplot 使用哪个颜色映射。
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor="none",s=40)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 函数axis() 要求提供四个值:x和y坐标轴的最小值和最大值。
plt.axis([0, 1100, 0, 1100000])
plt.tick_params(axis="both", which="major", labelsize=14)

plt.show()
# 要让程序自动将图标保存到文件中，可将对plt.show()的调用替换为对plt.savafig()的调用：
# 第一个实参指定要以什么样的文件名保存图表，这个文件将储存到scatter_squares.py所在的目录中;
# 第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白曲剧，可省略这个实参

plt.savafig("squares_plot.png", "bbox_inches"="tight")

