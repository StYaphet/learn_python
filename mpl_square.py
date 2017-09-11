import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
# 参数linewidth决定了plot() 绘制的线条的粗细。
plt.plot(input_values, squares, linewidth=5)

# 设置图表标题，并给坐标轴加上标签
# 函数title()给图表指定标题。
# fontsize 指定了图表中文字的大小。
plt.title("Square Numbers", fontsize=24)
# 函数xlabel() 和ylabel() 让你能够为每条轴设置标题
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 而函数tick_params()设置刻度的样式
# 其中指定的实参将影响x轴和y轴上的刻度 (axes='both')，并将刻度标记的字号设置为14(labelsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()
