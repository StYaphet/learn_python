import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename_1 = "death_valley_2014.csv"
filename_2 = "sitka_weather_2014.csv"

with open(filename_1) as f:
    # 我们调用csv.reader(),并将前面存储的文件对象作为实参传递给它,从而创建一个与该文件相关联的阅读器(reader)对象
    reader = csv.reader(f)
    # 模块csv包含函数next(),调用它并将阅读器对象传递给它时,它将返回文件中的下一行。
    # 我们只调用了next()一次，因此得到的是文件的第一行，其中包含文件头
    header_row = next(reader)

    # 为让文件头数据更容易理解，将列表中的每个文件头及其位置打印出来:
    # 我们对列表调用了enumerate()来获取每个元素的索引及其值。
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates_1, highs_1, lows_1 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            # 将包含日期信息的数据（row[0]）转换为datatime对象，并将其添加进dates列表
            dates_1.append(current_date)
            highs_1.append(high)
            lows_1.append(low)

with open(filename_2) as f:

    reader = csv.reader(f)
    header_row = next(reader)
    dates_2, highs_2, lows_2 = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            # 将包含日期信息的数据（row[0]）转换为datatime对象，并将其添加进dates列表
            dates_2.append(current_date)
            highs_2.append(high)
            lows_2.append(low)

fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates_1, highs_1, c="red")
plt.plot(dates_1, lows_1, c="blue")
# 使用方法fill_between()，它接受一个x值系列和两个y值系列，并填充两个y值系列之间的空间
# alpha指定颜色的透明度，
plt.fill_between(dates_1, lows_1, highs_1, facecolor="blue", alpha=0.1)

plt.plot(dates_2, highs_2, c="green")
plt.plot(dates_2, lows_2, c="yellow")
plt.fill_between(dates_2, lows_2, highs_2, facecolor="purple", alpha=0.1)

plt.title("Daily high temperatures - 2014", fontsize=24)
plt.xlabel("", fontsize=16)
# 调用fig.autofmt_xdate()来绘制日期标签，以免他们彼此重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis="both", labelsize=16)
# 将y轴的坐标值范围设定在10-130之间
plt.ylim(10, 130)
plt.savefig("compare temperatures.svg") 
plt.show()
