import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:

    rw = RandomWalk(50000)
    rw.fill_walk()

    plt.figure(figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
# 我们将参数c 设置为point_numbers ，指定使用颜色映射Blues ，并传递实参edgecolor=none 以删除每个点周围的轮廓。
    plt.scatter(rw.x_values, rw.y_values,
                c=point_numbers, cmap=plt.cm.Blues, s=1)
    plt.scatter(0, 0, c="green", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == "n":
        break
