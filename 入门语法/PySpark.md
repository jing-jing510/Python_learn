# PySpark

## 数据输入
```python
from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "../python.exe"
conf = SparkConf().setMaster("Local[*]").setAppName("test")

sc = SparkContext(conf=conf)
# 数据输入
rdd = sc.parallelize([1,2,3,4,5]) # list dict str set tuple 都可以
print(rdd.collect())

rdd1 = sc.textFile("path") #文本
```
## 数据计算
### map
```python
def func(data):
    return data * 10

rdd1 = rdd.map(func)
rdd2 = rdd.map(lambda x: x * 10)
# func (T) -> U 有个参数 有个返回值
```
接受一个处理函数,可以用lambda ,对每个元素逐个处理
### flatMap
* 对rdd进行map操作,然后进行接触嵌套操作
### ReduceByKey
* 针对KV型RDD,自动按照KEY分组,然后根据聚合逻辑,进行value操作
```python
rdd.reduceByKey(func)
# func:(v,v) ->v
```
* 接受2个传入参数(类型要一致),返回一个返回值,类型和传入要求一致
