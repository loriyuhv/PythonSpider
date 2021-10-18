import re

# () 匹配目标
"""
content = "Hello 1234567 world_This is a Regex Demo."
result = re.match("^Hello\s(\d+)\sworld.(\w+)\sis", content)
print(result.group())           # 输出完整的匹配结果
print(result.group(1))          # 输出()包含的结果
print(type(result.group(1)))    # 类型是str
print(result.groups())          # 输出()包含的所有结果
# print(type(result.groups()))    # 类型是tuple
"""

# 贪婪与非贪婪
"""
content = "IHello 1234567 world_This is a Regex Demo."
# 想要结果为1234567
# 贪婪匹配 .*
result = re.match(r'^IHe.*(\d+).*Demo\.$', content)
print(result.group(1))  # 输出7

# 非贪婪匹配 .*? ?就是匹配一次或不匹配
result = re.match(r'^IHe.*?(\d+).*Demo\.$', content)
print(result.group(1))
# 贪婪
result_x = re.match(r'^I.*(\w+)\s', content)    # .*是以匹配到整个字符创结尾“\s”这的
print(result_x.group(1))    # 输出：x
# 所以，想要结果为o，必须：否则以上输出：x
result_o = re.match(r"^I.*(\w+)\s12", content)
print(result_o.group(1))  # 输出：o
# 想要结果为Hello
result_Hello = re.match(r"^I.*?(\w+)\s12", content)
print(result_Hello.group(1))
"""


#

