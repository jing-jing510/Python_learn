# Python_learn

## Format函数

在Python中，字符串对象的format（）方法提供了一种灵活的方式，将变量、表达式和其他值插入到字符串中。格式化字符串的一般形式是在字符串中使用大括号{}作为占位符，然后使用format()方法来为这些占位符提供值。

例如，我们可以把一个字符串的两个占位符替换为两个变量：

```
name = "Alice"
age = 30
print("My name is {} and I'm {} years old.".format(name, age))
```

这将输出：

```
My name is Alice and I'm 30 years old.
```

可以看到，format（）方法将字符串中的第一个占位符替换为name变量的值，将第二个占位符替换为age变量的值。

另外，我们也可以使用格式说明符来控制变量的输出格式。例如，我们可以使用以下代码将数字四舍五入到小数点后两位：

```
price = 19.99
print("The price is {:.2f} dollars.".format(price))
```

这将输出：

```
The price is 19.99 dollars.
```

在这个例子中，我们使用{:.2f}作为占位符，并将其放入format（）方法中。这告诉Python将变量price格式化为带有两位小数的浮点数（float）。

除了使用位置参数之外，我们还可以使用命名参数来代替位置参数。这可以使代码更加易于阅读。例如：

```
print("Hello, {name}. You are {age} years old.".format(name="Alice", age=30))
```

这将输出：

```
Hello, Alice. You are 30 years old.
```

除了字符串，format（）方法还可以用于其他数据类型，例如整数和布尔值。例如：

```
print("The answer is {}.".format(42))
print("Is it raining outside? {}.".format(True))
```

这将输出：

```
The answer is 42.
Is it raining outside? True.
```

在总结上，format（）方法是一种非常灵活的向Python字符串中插入值的方法。它可以使用位置参数、命名参数和格式说明符，并支持多种数据类型。

## strip函数
在Python中，strip()是一个内置函数，用于删除字符串开头和结尾处的空格或指定字符。strip()函数返回一个新字符串，原始字符串不会被修改。

strip()函数的语法如下：

```python
string.strip([chars])
```

其中，`string`是要操作的字符串；`chars`是可选参数，表示要删除的指定字符，默认为空格。

下面是一些示例：

```python
string = " Hello, World! "
print(string.strip())  # "Hello, World!"
```

上述代码中， `strip()`函数会删除字符串开头和结尾的空格，返回一个新字符串。

```python
string = "-----Hello, World!-----"
print(string.strip('-'))  # "Hello, World!"
```

上述代码中，`strip('-')`函数会删除字符串开头和结尾的连字符（"-"），返回一个新字符串。

注意，`strip()`函数只能删除开头和结尾的字符，而不能删除字符串中间的字符。如果您想删除字符串中间的字符，可以使用 `replace()` 函数替换掉目标字符或者使用正则表达式。
