import re

"""
^：匹配字符串开头
$：匹配字符串结尾
\b：匹配一个单词的边界
\B：匹配非单词边界
"""

# ^ 匹配字符串开头
"""
content = "I wanted to be an free engineer."
result = re.search(r"^I.*(en.*er\b)", content)
print(result.group(1))
"""

# 示例1：$：匹配字符串结尾
"""
需求：匹配163.com的邮箱地址
# 正确的地址
result = re.match(r"[\w]{4,20}@163\.com", "loriyuhv@163.com")
print(result.group())

# 不正确的地址
result = re.match(r"[\w]{4,20}@163\.com", "loriyuhv@163.com.haha")
print(result.group())

# 通过$来确定末尾 $：匹配字符串结尾
result = re.match(r"[\w]{4,20}@163\.com$", "loriyuhv@163.com.haha")
print(result.group())   # 出错：因为字符串结尾是haha 不是com所以报错
"""

# 示例2：\b：匹配一个单词的边界
"""
result = re.match(r".*\bver\b", "ho ver abc").group()
print(result)

result = re.match(r".*\bver\b", "ho ver.abc").group()
print(result)

result = re.match(r".*\bver\b", "hover abc").group()
print(result)
"""

# 示例3：\B：匹配非单词的边界
"""
result = re.match(r".*\Bver\B", "hoverabc").group()
print(result)

# result = re.match(r".*\Bver\B", "ho verabc").group()
# 改正：
result = re.match(r".*\bver\B", "ho verabc").group()
print(result)   # 出错 ver前端有边界：出错，后端无边界：没问题

# result = re.match(r".*\Bver\B", "hover abc").group()
# 改正
result = re.match(r".*\Bver\b", "hover abc").group()
print(result)   # 出错 ver前端无边界：没问题，后端有边界：出错

# result = re.match(r".*\Bver\B", "ho ver abc").group()
# 改正
result = re.match(r".*\bver\b", "ho ver abc").group()
print(result)   # 出错 前后端都有边界：出错
"""



