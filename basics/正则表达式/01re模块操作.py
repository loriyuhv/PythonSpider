# 导入re模块
import re

content = "apple"

# 使用match方法进行匹配操作
result = re.match('apple', content)     # 'apple'：正则表达式。 content：匹配的字符串

# 如果上一步匹配到数据的话，可以用group方法来提取数据
print(result.group())

# 示例
# 需求：匹配以taobao开头的语句

result = re.match("taobao", "taobao.com")
print(result.group())

