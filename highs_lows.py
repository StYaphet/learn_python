import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = "sitka_weather_2014.csv"
with open(filename) as f:
    # 我们调用csv.reader(),并将前面存储的文件对象作为实参传递给它,从而创建一个与该文件相关联的阅读器(reader)对象
    reader = csv.reader(f)
    # 模块csv包含函数next(),调用它并将阅读器对象传递给它时,它将返回文件中的下一行。
    # 我们只调用了next()一次，因此得到的是文件的第一行，其中包含文件头
    header_row = next(reader)

    # 为让文件头数据更容易理解，将列表中的每个文件头及其位置打印出来:
    # 我们对列表调用了enumerate()来获取每个元素的索引及其值。
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        # 将包含日期信息的数据（row[0]）转换为datatime对象，并将其添加进dates列表
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])
        low = int(row[3])
        highs.append(high)
        lows.append(low)

    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red")
    plt.plot(dates, lows, c="blue")
    plt.fill_between(dates, lows, highs, facecolor="blue", alpha=0.1)

    plt.title("Daily high temperatures - 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    # 调用fig.autofmt_xdate()来绘制日期标签，以免他们彼此重叠
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis="both", labelsize=16)

    plt.show()
