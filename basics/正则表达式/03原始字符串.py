import re

content = "c:\\a\\b\\c"
"""
print(content)    # 输出：c:\a\b\c
result = re.match("c:\\\\", content).group()
print(result)

result = re.match("c:\\\\a", content).group()
print(result)	# 输出：c:\a

result = re.match(r"c:\\a", content).group()
print(result)	    # 输出：c:\a

# 出错 因为r是原生字符串，所以\a匹配的是\。改正：\ 可以用转义字符：\ 也可以用\W . 等
result = re.match(r"c:\a", content).group()
print(result)

"""

