import re

content = "c:\\a\\b\\c"
# print(content)  # 输出：c:\a\b\c

# result = re.match("c:\\\\", content).group()
# print(result)   # 输出：c:\ 本应该输出：c:\\

# result = re.match("c:\\\\a", content).group()
# print(result)   # 输出：c:\a

result = re.match(r"c:\\a", content).group()
print(result)   # 输出：c:\a
