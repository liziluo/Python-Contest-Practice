import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


years = [2015, 2016, 2017, 2018 , 2019 ,2020]
gdp = [72812.55,80854.91,89705.23,99945.22,107671.07,110760.94]
plt.bar(years, gdp)
plt.title('广东省GDP情况')


plt.show()

