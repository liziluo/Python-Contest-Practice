import matplotlib.pyplot as plt
import numpy as np

# 这两行代码解决 plt 中文显示的问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


years = [2015, 2016, 2017, 2018 , 2019 ,2020]
sport=[9684.07,10511.14,13007.26,13992.33,16150.66,8860.88]
plt.bar(years, sport)
plt.title('广东省体育产业收入')


plt.show()

