import re
"""
|：匹配左右任意一个表达式

"""

# 示例1：|：匹配左右任意一个表达式
"""
# 需求：匹配出0-100之间的数字
result = re.match(r'[0-9]?\d', '8').group()
print(result)

result = re.match(r'[0-9]?\d', '78').group()
print(result)

# 不正确的情况
result = re.match(r"[0-9]?\d", "08").group()
print(result)   # 只能匹配到：0

# 修正之后

# 可以匹配0~99的数字 但匹配100出错
result = re.match(r"[0-9]?\d$", "100")
print(result.group())

# 修正之后，可以匹配0~100
result = re.match(r"[0-9]?\d$|100", "08")
print(result.group())
"""

# 示例2：(ab)：将括号中字符作为一个字符
"""
# 需求：匹配出163、126、qq邮箱之间的数字
ret = re.match(r"\w{4,20}@163\.com", "test@163.com")
print(ret.group())

ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@126.com")
print(ret.group())

ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@qq.com")
print(ret.group())

ret = re.match(r"\w{4,20}@(163|126|qq)\.com", "test@gmail.com")
print(ret.group())  # 出错

# 练习
ret = re.match(r"([^-]*)-(\d+)", "010-12345678")
print(ret.group())
print(ret.groups())     # 输出：('010', '12345678')
"""

# 示例3：\
"""
# 需求：匹配出<html>hh</html>
# 能够完成对正确的字符串的匹配
content = "<html>hh</html>"
ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", content)
print(ret.group())

# 如果遇到非正常的html格式字符串，匹配出错
ret = re.match(r"<[a-zA-Z]*>\w*</[a-zA-Z]*>", "<html>hh</htmlbalabala>")
print(ret.group())  # 输出：<html>hh</htmlbalabala>

# 正确的理解思路：如果在第一对<>中是什么，按理说在后面的那对<>中就应该是什么
# 通过引用分组中匹配到的数据即可，但是要注意是元字符串，即类似 r""这种格式
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", content)
print(ret.group())

# 因为2对<>中的数据不一致，所以没有匹配出来
ret = re.match(r"<([a-zA-Z]*)>\w*</\1>", "<html>hh</htmlbalabala>")
ret.group()
"""

# 示例4：\number: 引用number别名的字符串
"""
# 需求：匹配出<html><h1>www.taobao.com</h1></html>
content = "<html><h1>www.taobao.com</h1></html>"
# ret = re.match(r"<([a-zA-Z]*)><([a-zA-Z0-9]*)>.*</\2></\1>", content)
ret = re.match(r"<(\w*)><(\w*)>.*</\2></\1>", content)
print(ret.group())
"""

# 示例5：(?P<name>)：分组起别名 (?P=name)：引用别名为name分组匹配到的字符串
# 需求：匹配出<html><h1>www.taobao.com</h1></html>
content = "<html><h1>www.taobao.com</h1></html>"
ret = re.match(r"<(?P<label1>\w*)><(?P<label2>\w*)>.*</(?P=label2)></(?P=label1)>", content)
print(ret.group())






