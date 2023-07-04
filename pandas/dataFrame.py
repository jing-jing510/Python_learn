# auth ： xiaokou
# date ： 2023/7/4 11:12
import numpy as np
import pandas as pd

# 创建一个包含学生信息的DataFrame
data = {
    '姓名': ['小明', '小红', '小刚', '小亮'],
    '年龄': [18, 20, 19, 22],
    '成绩': [85, 92, 88, 78]
}
df = pd.DataFrame(data)

print(df)
print('-------------------')
print(df['姓名'])  # 输出姓名列的数据
df['性别'] = ['男', '女', '男', '男']  # 添加性别列
print('-------------------')
print(df)
print('-------------------')
filtered_df = df[df['成绩'] > 90]  # 筛选成绩大于90的行
print(filtered_df)

print('-------------------')
# 选择数值列，并计算平均值
numeric_cols = ['年龄', '成绩']
numeric_mean = df[numeric_cols].mean()
print(numeric_mean)

# 访问和修改元素：
df.loc[0, '姓名']  # 访问第一行，'姓名'列的元素
df.iloc[1, 2]  # 访问第二行，第三列的元素

df.loc[0, '姓名'] = '小李'  # 修改第一行，'姓名'列的元素
df.iloc[1, 2] = 95  # 修改第二行，第三列的元素

# 筛选行和列：
filtered_df = df[df['成绩'] > 90]  # 筛选成绩大于90的行
selected_cols = df[['姓名', '年龄']]  # 选择特定的列
print(filtered_df)
print(selected_cols)

# 使用sort_values()对DataFrame进行排序操作
sorted_df = df.sort_values(by='成绩', ascending=False)  # 按照'成绩'列降序排序
print(sorted_df)

# 增加和删除列：
# 使用赋值操作符添加新的列，使用drop()删除列。
df['性别'] = ['男', '女', '男', '男']  # 添加'性别'列
df = df.drop('年龄', axis=1)  # 删除'年龄'列
# 缺失值处理：
# 使用isnull()检查缺失值，使用dropna()删除包含缺失值的行或列，使用fillna()填充缺失值。
df.isnull()  # 检查缺失值
df = df.dropna()  # 删除包含缺失值的行
df = df.fillna(0)  # 将缺失值填充为0
# 分组和聚合：
# 使用groupby()将数据按照某个列进行分组，然后使用聚合函数进行计算。
# grouped_df = df.groupby('成绩').mean()  # 按照'性别'列进行分组并计算平均值

print(df.columns)
print(df.index)
print(df.columns.tolist())
print(df.index.tolist())