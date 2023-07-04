# auth ： xiaokou
# date ： 2023/7/4 16:35
# 如果txtFile中的1.txt不存在，那么写入
import os

if not os.path.exists('txtFile'):
    os.mkdir('txtFile')
fs = open('txtFile/1.txt', 'w')
print('hello world',file=fs)
fs.close()

with open('txtFile/2.txt', 'w') as fs:
    print('hello world',file=fs)