# Flask 快速开发
> pip3 install flask

## 引用

```python
@app.route('/show/info')
def index():
    # return 'index'
    return render_template('index.html')
```

这里@app.route()为访问地址

render_tmplate 是展示templates下的index.html

## 浏览器能识别的标签

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>测试</title>
</head>
<body>
    <h1>你好~ 哈哈哈哈</h1>
    <div>
        快标签
    </div>
    <span>行标签</span>
    <p>
        段落
    </p>
    <a href="index.html">超链接标签</a>
<!--    也可以这么写-->
    <a href="/get/news">直接跳转方法</a>
<!--    显示自己的图片放在static-->
    <img src="">
</body>
</html>
</html>
```

```html
<ul>
    <li>无序列表</li>
    <li></li>
</ul>
<ol>
    <li>有序列表</li>
</ol>
<!-- 表格 -->
<table>
    <thead> 
    	<tr>
        	<th>表头</th>
            <th>有多少列</th>
        </tr>
    </thead>
    <tboby>
    	<tr>
        	<td>表内容</td>
            <td>一行数据</td>
        </tr>
    </tboby>
</table>
```



