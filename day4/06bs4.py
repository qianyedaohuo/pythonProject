"""
 beautifulSoup 是一个可以从html或xml文件中提取数据的Python库
"""
from bs4 import BeautifulSoup

# 创建一个对象   html.parser 通用的解码器

html = ""

soup = BeautifulSoup(html, 'html.parser')

print(soup)

# find 方法,默认只返回一个内容，如果没有找到，返回None
# find('标签名称' ,attrs{"属性名称":"对应的属性值"})
