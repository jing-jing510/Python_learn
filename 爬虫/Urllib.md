# Urllib
不知道有没有人跟我一样想过这个问题，Python怎么会有那么多网络请求的库urllib、urllib2...这我到底要用哪一个，几个库又有什么区别，真是让人头大，下文我就针对urllib、urllib2、urllib3来做一个详细的阐述。

## 简介
urllib、urllib2、urllib3均能通过网络访问互联网上的资源文件，它们通过使用统一资源定位符（URL）并结合re模块完成很多意想不到的操作

1. urllib：Python2和Python3内置的网络请求库，Python3的urllib实际是Python2版本中urllib和urllib2的合并
2. urllib2：它只存在于Python2版本的内置库中，功能与urllib基本类似，主要上urllib的增强
3. urllib3：Python2和Python3均可以使用，但这不是标准库，需要使用pip安装使用，urllib3提供了线程安全池和文件post等

## Get请求
```python
from urllib import request

res = request.urlopen("http://www.baidu.com")
print(res.read())
```