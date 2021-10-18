import re

# a = "taobao.com"
# result = re.match("taobao", a)
# print(result.group())
# print(result)
# print(type(result))

# .能匹配任意一个字符
# data = "I wanted to be an engineer."
# result = re.match(".", data)

# \d 匹配数字
# data = "1234567"
# result = re.match("\d", data)

# \D 匹配非数字
# data = "1W"
# result = re.match("\D", data)  # 报错，因为match是从头开始匹配
# data2 = "I wanted to bake the goat."
# result = re.match("\D", data2)

# \s 匹配空格
# data = "I wanted"
# result = re.match("\D\s\D", data)

# \S 匹配非空白
# data = "\nI wanted to"
# result = re.match("\S\S\D", data) # 错误，因为\n是转义字符
# data = "I want"
# result = re.match("\S", data)

# \w 匹配字符 a-z A-Z 0-9
# data = "I wanted"
# result = re.match("\w", data)

# \W 匹配非字符 \n \r这种
# data = "\nI"
# result = re.match("\W\w", data)
# print(result.group())

# 如果hello的首字符小写，那么正则表达式需要小写的h
# ret = re.match("h", "hello Python")
# print(ret.group())


# 如果hello的首字符大写，那么正则表达式需要大写的H
# ret = re.match("H", "Hello Python")
# print(ret.group())

# 大小写h都可以的情况
# ret = re.match("[hH]", "hello Python")
# print(ret.group())
# ret = re.match("[hH]", "Hello Python")
# print(ret.group())

# 匹配0到9第一种写法
# ret = re.match("[0123456789]", "7Hello Python")
# print(ret.group())

# 匹配0到9第二种写法
# ret = re.match("[0-9]", "7Hello Python")
# print(ret.group())

# 匹配中文字符
# data = "我想去远方。"
# print(re.match(".", data).group())
# print(re.match("\w", data).group())
# print(re.match("\D", data).group())
# print(re.match("[\u4e00-\u9fa5]", data).group())
# print(re.match("\S", data).group())
# print(re.match('.', data, re.ASCII).group())

# data = "I wanted to go to Beijing"
# *匹配前一个字符出现0次或无数次
# print(re.match('.*to', data).group())
# print(re.match('\w*\s\w*', data).group())

# + 匹配前一个字符出现一次或无限次 至少有一次
# data = " I wanted to go to Beijing"
# 与*的区别
# print(re.match('\w*\s\w\s\w+', data).group()) # 可有可无
# print(re.match('\w+\s\w\s\w+', data).group()) # 至少有一次

# ? 匹配前一个字符出现一次或者零次 可有可无
# data = "I wanted to go to Beijing"
# data1 = " I wanted to go to Beijing"
# print(re.match("\w?\s\w\s\w?", data1).group())
# print(re.match('\w?\s\w?', data).group())

# {m} 匹配前一个字符出现m次
# data = "tooth"
# print(re.match('\w{5}', data).group())

# {m,} 匹配一个字符至少出现m次
# data = "wanted I"
# print(re.match('\w{3,}', data).group())

# {m,n} 匹配一个字符出现从m次到n次
# data = "hit me"
# print(re.match('\w{1,3}', data).group())


# 需求：匹配出，一个字符串第一个字母为大写字符，后面都是小写字母并且这些小写字母可有可无
# data = "Name"
# data1 = "I wanted"
# print(re.match(r'[A-Z][a-z]*', data).group())
# print(re.match(r'[A-Z][a-z]*', data1).group())

# 需求：匹配出，变量名是否有效
# 命名规则 可以以下划线开头，大小写字母开头

# ret = re.match(r"[a-zA-Z_]+[\w_]*", "name1")
# print(ret.group())

ret = re.match(r"[a-zA-Z_]+[\w_]*", "_name")
print(ret.group())
#
# ret = re.match("[a-zA-Z_]+[\w_]*", "2_name")
# ret.group()



