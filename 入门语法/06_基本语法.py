# auth ： xiaokou
# date ： 2023/5/23 10:36

# 标识符命名规则
"""
    只允许 英文 中文 数字 _
    不推荐使用中文
    数字不可以开头
    大小写敏感 Andy  andy
    不可以使用关键字 False True None And as assert break class continue
"""
name_ = "1"
_name = "2"
Andy = "3"
andy = "4"
print(name_, _name, Andy, andy)
print("---------------")

# 变量的命名规范
"""
    多个单词组合变量名,使用下划线做分割
    英文字母全小写
"""
Password_zhangsan = 5

print("------------")

# 算术运算符 + - * / // % **
"""
    / 是除
    // 取整除
    % 取余
    ** 指数
    赋值运算符 1 + 2 * 3 
    符合赋值运算符 += -= *= /= //= %= **=
"""
print("5/2:", 5 / 2)  # 2.5
print("5//2:", 5 // 2)  # 2
print("5//2:", 5 % 2)  # 1
print("5**2:", 5 ** 2)  # 25
print("--------------")

# 字符串
"""
    定义方式 name='1' name = "2" 还有三引号
    转义字符 "\"  将 ' " 可以转义
    字符串拼接: +号连接
    字符串格式化: 变量过多,不好拼接,所以使用格式化 %s :占位符  %s 字符串 %d 整数 %f 浮点数
                m.n 控制数据的宽度和精度  %5d 宽度5位 例如 11: ___11  _这里代表空格
                                      %5.2d 宽度5 小数精度2 ___11 
                                      %5.2f 宽度5 小数精度2 ___11.00
    格式化2:   f"{name}"   原文输出,不用理会类型
"""
print("1" + "2")
name = "1"
add = "2"
age = 18
print("字符串变量和字符窜字面量拼接" + name + "再来一个:" + add)
print("站位 %s 和 %s" % (name, add))
print("站位 %s 和 %s 和 %d" % (name, add, age))
print("站位 %s 和 %s 和 %5.2f" % (name, add, age))
print(f"name:{name}")
print("-----------")
# 小练习 name stock_price stock_code ,stock_price_daily_growth_factor,growth_days
name = "1"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_days = 7
print(f"公司为:{name},股票代码:{stock_code},当前股价:{stock_price}")
print("每日增长系数为: %.1f,经过%d天的增长后,股价达到了:%.2f" % (
    stock_price_daily_growth_factor, growth_days, stock_price * stock_price_daily_growth_factor ** growth_days))
print("--------------")
# input语句  接收数据  input("这里可以填写提示")  输入的都是字符串类型 如若需要记得转型

# 判断语句
"""
    boolean类型 True False
    运算符 == != > < >= <=
"""

# if语句
"""
    if 判断条件:
        成立做什么.
    elif 判断条件:
        成立做什么
    else :
        否则做什么
"""
# age = int(input("输入你的年龄"))
# if age >= 18:
#     print("欢迎广陵")
#     print("男宾一位,补票10元")
# else:
#     print("做小孩儿那桌去")
# print("结束游玩")

# 案例 定义一个数字(1-10)随机产生 ,通过三次判断来猜数字
# import random
#
# num = random.randint(1, 10)
# num1 = int(input("来猜猜数字:"))
# if num1 != num:
#     if num1 > num:
#         num2 = int(input("猜大了,再来"))
#     else:
#         num2 = int(input("猜小了,再来"))
#     if num2 != num:
#         if num2 > num:
#             num3 = int(input("猜大了,最后一次了,再来"))
#         else:
#             num3 = int(input("猜小了,最后一次了,再来"))
#     else:
#         print("恭喜你,第二次才对啦")
#     if num3 != num:
#         print("三次机会用完了,猜错了吧,正确答案是:", num)
#     else:
#         print("恭喜你,第三次才对啦")
# else:
#     print("恭喜你第一次就猜对了,数字为", num)

# while 循环
"""
    while 条件:
        满足做的事情 1  2  3
        
"""
# 其1-100的和
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1

print("1-100的和为:", sum)

# 猜数字
# import random
#
# num = random.randint(1, 100)
# print(num)
# count = 1
# while int(input("请输入数字")) != num:
#     count += 1
# print("不容易 猜对了,总共猜了:", count)

# for 循环
"""
    for x in name:
        print(x)
    无法定义循环条件,只能被动取出数据
    要注意 空格缩进
    对于临时变量x 外部可以访问,但不建议
"""
name ="lijing"
for x in name:
    print(x)
# 数一数有几个a
name ="yahhh is a brand of itcast"
count =0
for x in name:
    if x == "a":
        count += 1
print(f"{name}一共有:{count}个a")

# rang语句
"""
    生成序列
    range(num) 0~num-1 range(num1,num2,step) range(num1,num2) 左闭右开
"""
# 案例 有几个偶数
print("有几个偶数")
num=100
count = 0
for x in range(1,100):
    if x%2==0:
        count+=1
print(f"1到{num}总共有,{count}个偶数")
print("-----------------")
print("9*9乘法表")
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} ={j*i}\t", end='')
    print()
