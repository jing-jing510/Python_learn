# auth ： xiaokou
# date ： 2023/7/4 11:23

import pandas as pd

# 访问元素
s = pd.Series([1, 2, 3, 4, 5])
# print(s[0])
print(s[2:4])   # 不包含4

#算术运算
s1 = pd.Series([1, 2, 3 ])
s2 = pd.Series([4,5,6])
s3 =s1 +s2
print(s3)  # 进行加法

s = pd.Series([1, 2, 3, 4, 5])
print(s.sum())  # 求和
print(s.mean())  # 均值
print(s.max())  # 最大值
print(s.min())  # 最小值

s = pd.Series([1, 2, 3, 4, 5])
print(s[s > 3])  # 筛选大于3的元素
print(s[:3])  # 切片前三个元素

s = pd.Series([3, 1, 4, 2, 5])
s_sorted = s.sort_values()  # 按值排序
print(s_sorted)

import numpy as np
import pandas as pd

s = pd.Series([1, np.nan, 3, np.nan, 5])
print(s.isnull())  # 检查缺失值
s_cleaned = s.dropna()  # 删除缺失值
print(s_cleaned)

