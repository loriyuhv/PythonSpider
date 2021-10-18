import re

# * 匹配前一个字符出现0次或无数次
"""
data = "I wanted to go to Beijing"
print(re.match('.*to', data).group())
print(re.match('\w*\s\w*', data).group())
"""

# + 匹配前一个字符出现一次或无限次 至少有一次
"""
data = " I wanted to go to Beijing"
# 与*的区别
print(re.match(r'\w*\s\w\s\w+', data).group())  # 可有可无
print(re.match(r'\w+\s\w\s\w+', data).group())  # 至少有一次
"""

# ? 匹配前一个字符出现一次或者零次 可有可无
"""
data = "I wanted to go to Beijing"
data1 = " I wanted to go to Beijing"
print(re.match('\w?\s\w?', data).group())
print(re.match("\w?\s\w\s\w?", data1).group())
"""

# {m} 匹配前一个字符出现m次
"""
data = "tooth"
print(re.match('\w{5}', data).group())
"""

# {m,} 匹配一个字符至少出现m次
"""
data = "wanted I"
print(re.match('\w{3,}', data).group())
"""

# {m,n} 匹配一个字符出现从m次到n次
"""
data = "hit me"
print(re.match('\w{1,3}', data).group())
"""

# 需求：匹配出，一个字符串第一个字母为大写字符，后面都是小写字母并且这些小写字母可有可无
"""
data = "Name"
data1 = "I wanted"
print(re.match(r'[A-Z][a-z]*', data).group())
print(re.match(r'[A-Z][a-z]*', data1).group())
"""

# 需求：匹配出，变量名是否有效
"""
# 命名规则 可以以下划线开头，大小写字母开头
ret = re.match(r"[a-zA-Z_]+[\w_]*", "name1")
print(ret.group())

ret = re.match(r"[a-zA-Z_]+[\w_]*", "_name")
print(ret.group())

ret = re.match("[a-zA-Z_]+[\w_]*", "2_name")
ret.group()
"""