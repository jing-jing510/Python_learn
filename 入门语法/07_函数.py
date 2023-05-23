# auth ： xiaokou
# date ： 2023/5/23 15:52

# 函数 组织好的,可以重复使用,用来实现特定功能的代码段.
"""
    def 函数名(参数名):
        函数体
        return 返回值
    先定义函数,后调用函数
    传参:用逗号进行分割,按照顺序输入 数量不受限制
    返回值: return后面的值都不运行  不返回那就是None
    None:NoneType的字面量 空白的意思
    说明文档: 三引号 自动生成
    嵌套调用:在一个喊舒总,调用另外一个函数.
    局部变量:在函数体内定义的变量,在外边无法使用
    全局变量:在函数体外定义的变量,哪里都可以使用  函数修改,外部还是原来的值(因为不是一个值) 如果添加global 就会变化
"""
# def add(x,y):
#     """
#     两数字相加
#     :param x:
#     :param y:
#     :return:
#     """
#     res = x+y
#     print(res)
#     return res
money =5000000
print("""
-------主菜单---------
吴彦祖,你好,欢迎来到银行ATM,请选择操作:
查询余额   [输入1]
存款      [输入2]
取款      [输入3]
退出      [输入4]
请输入您的选择
""")
def chaxun():
    print(f"您的余额为:{money}")

def cunqian():
    num =int(input("请输入您要存多少钱"))
    global money
    money += num
    chaxun()

def quqian():
    num = int(input("请输入您要取多少钱"))
    global money
    if num<money:
        money -= num
    else:
        print("您的余额不足,请重新操作")
    chaxun()
flag =True
while flag :
    zhiling = int(input())
    if zhiling == 1:
        chaxun()
    elif zhiling ==2:
        cunqian()
    elif zhiling ==3:
        quqian()
    elif zhiling == 4:
        print("感谢使用,欢迎下次光临")
        flag=False
        break
    else:
        print("输入错误,请重新输入")