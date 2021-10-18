import re

with open('test.html', 'r', encoding='gbk') as f:
    html = f.read()

result = re.search(r'<div\sclass="novelslist">.*<div\sclass="clear"></div>', html, re.S)

with open('test1.html', 'w', encoding='gbk') as f:
    f.write(result.group())

with open('test1.html', 'r', encoding='gbk') as f:
    html = f.read()

# 分类
title_results = re.findall(r'<h2>(.*?)</h2>', html, re.S)
# print(title_results)


def get_data(content):
    # <a href="http://www.b520.cc/2_2157/">太古神王</a>/净无痕
    results = re.match(r'<a\shref="(.*?)">(.*?)</a>/(.*?)', content, re.S)
    print("书名：" + results.group(2) + " 作者：" + results.group(3) + " 链接：" + results.group(1))
    pass


def parse_ul(html):
    results = re.findall(r'<li>(.*?)</li>', html, re.S)
    for result in results:
        get_data(result)
    pass


# ul拿出来了
results = re.findall(r'<ul>.*?</ul>', html, re.S)
for i in range(0, len(results)-2):
    print(title_results[i])
    parse_ul(results[i])
    print("*"*20)


