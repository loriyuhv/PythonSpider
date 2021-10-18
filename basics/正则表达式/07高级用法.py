import re

# search
"""
content = "Hello 1234567 world_This is a Regex Demo."
result = re.search(r"\s(\d+)\swo", content)
print(result.group(1))

# 需求：匹配出文章阅读的次数
ret = re.search(r"\d+", "阅读次数为：9999")
print(ret.group())
"""

# findall
"""
content = "Hello 1234567 world_This is a Regex Demo." \
          " 7654321 world"
result = re.findall(r"\s(\d+)\swo", content, re.S)
print(result)
"""

# sub
"""
content = "Hello 1234567 world_This is a Regex Demo." \
          " 7654321 world"
result = re.sub(r"\s\d+", "", content)
print(result)

# 需求：将匹配到的阅读次数加1
def add(temp):
    # print(type(temp))   # re.Match
    # print(temp)     # <re.Match object; span=(9, 12), match='997'>
    strNum = temp.group()   # strNum: 997
    # print(strNum)
    num = int(strNum) + 1   # num 998 101
    # print(num) # 998 101
    return str(num)


ret = re.sub(r"\d+", add, "python = 997 java=100")
print(ret)
# print(type(ret))    # str

# ret = re.sub(r"\d+", add, "python = 99")
# print(ret)
"""

# compile
"""
content = "Hello 1234567 world_This is a Regex Demo."
pattern = re.compile(r".*?(\d+)\swo")
result = re.search(pattern, content)
print(result.group(1))
"""

content = """
<div>
    <p>岗位职责：</p>
    <p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
    <p><br></p>
    <p>必备要求：</p>
    <p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
    <p>&nbsp;<br></p>
    <p>技术要求：</p>
    <p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
    <p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
    <p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
    <p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
    <p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
    <p>&nbsp;<br></p>
    <p>加分项：</p>
    <p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>
</div>


result = re.findall(r"<(?P<label1>\w*)>(.*)</(?P=label1)>", content, re.S)

data = result[0][1].split('\n')
for i in data:
    write = re.match(r"<(?P<label1>\w*)>(.*)</(?P=label1)>", i.strip())
    if write != None:
        print(write.group(2))
"""
