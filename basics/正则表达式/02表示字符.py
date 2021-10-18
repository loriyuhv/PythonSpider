import re

# .能匹配任意一个字符
"""
data = "I wanted to be an engineer."
result = re.match(".", data)
"""

# \d 匹配数字
"""
data = "1234567"
result = re.match("\d", data)
"""

# \D 匹配非数字
"""
data = "1W"
result = re.match("\D", data)  # 报错，因为match是从头开始匹配
data2 = "I wanted to bake the goat."
result = re.match("\D", data2)
"""

# \s 匹配空格
"""
data = "I wanted"
result = re.match("\D\s\D", data)
"""

# \S 匹配非空白
"""
data = "\nI wanted to"
result = re.match("\S\S\D", data) # 错误，因为\n是转义字符
data = "I want"
result = re.match("\S", data)
"""

# \w 匹配字符 a-z A-Z 0-9
"""
data = "I wanted"
result = re.match("\w", data)
"""

# \W 匹配非字符 \n \r这种
"""
data = "\nI"
result = re.match("\W\w", data)
print(result.group())
"""

# 匹配中文字符
"""
data = "我想去远方。"
print(re.match(".", data).group())
print(re.match("\w", data).group())
print(re.match("\D", data).group())
print(re.match("[\u4e00-\u9fa5]", data).group())
print(re.match("\S", data).group())
print(re.match('.', data, re.ASCII).group())
"""

# 示例
"""
# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h", "hello Python")
print(ret.group())


# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H", "Hello Python")
print(ret.group())

# 大小写h都可以的情况
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]", "Hello Python")
print(ret.group())

# 匹配0到9第一种写法
ret = re.match("[0123456789]", "7Hello Python")
print(ret.group())

# 匹配0到9第二种写法
ret = re.match("[0-9]", "7Hello Python")
print(ret.group())
"""

