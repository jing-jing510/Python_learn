# auth ： xiaokou
# date ： 2023/5/23 16:24

"""
    可以容纳多份数据的Python数据类型
    list:   ['1','2','3',1,[1,2,3],True]
            下标索引: 从前往后 0开始  list[0]    list[4][1] =1
                    从后往前 -1开始递减
            常用方法: list.index(元素) 查元素的索引值
                     list[0]="" 重新复制
                     list.insert(下标,元素)  当前下标插入
                     list.append(元素)  追加
                     list.extend(其它容器) 追加新的list
                     del list[下标]  删除
                     list.pop(下标) 取出 病虫列表中删除
                     list.remove(元素)
                     list.clear() 清空
                     list.count() 计数  如果写参数 就是计算列表中 参数有几个
                     len(list) 长度
            总结:混装,有序,可重复,可修改
            遍历: 下标索引
    tuple: (元素,元素 ,元素) () tuple()
            支持下标索引 t[index]
            方法:    .count
                    len()
                    .index
            特点 多个数据 幻皇 有序,不可修改,但是可以修改内部list的元素
    str: "test"
        索引:my_str[2]  my_str[-1]
        不支持修改
        方法:    str.index("元素") 查找元素的起始坐标
                str.replace(字符串1,字符串2)
                str.split("分隔符")  可以获得一个新的list
                str.strip() 去除前后空格  如果添加字符串 去除前后字符串
                str.count("元素") 出现次数
                len(str) 长度
        特点:只可以字符串,长度任意,支持索引,允许重复,不可以修改
    序列:list tuple str 都是序列 内容连续 有序可以使用下标
        不影响原有数据,会创建新的原有类型
    set: {1,2,3,4,5}  set{1,2,3,4,5}  set()
        不支持索引,可以修改,无序的
        方法:
            set.add("2")
            set.remove("2")
            set.pop()  碎一个去,集合会发生变化
            set.clear() 清空
            set.difference(集合2)  取差
            set.difference_update(集合2) 取插 并删除 set中存在的
            set1.union(set2)  合并,并去重
            len(set1)
    dict:
"""
list1 = ["1", '2', '3', 1, [1, 2, 3], True]
print(list1)
print(type(list1))

print("----取出列表中的偶数----")
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
oushu_list = []
for x in my_list1:
    if x % 2 == 0:
        oushu_list.append(x)
print(oushu_list)

print("----------")
my_list = [0, 1, 2, 3, 4, 5]
res1 = my_list1[1:4]
print(res1)
print(type(res1))
my_tuple = (0,1,2,3,4)
res2 = my_tuple[:]
print(res2)
print(type(res2))
