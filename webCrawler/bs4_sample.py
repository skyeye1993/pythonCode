from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc) # 创建一个BeautifulSoup对象
print(soup.prettify())
print(soup.title)
print(soup.a.attrs['href']) # 取出a标签中的href属性
print(list(soup.p.children)) # 取出p标签下的所有子节点
print(soup.find_all('a')) #取出所有的a标签

for a in soup.find_all('a'):
    print(a.attrs['href']) #遍历所有a标签下得href属性

print(soup.find(id='link3')) # 取出id为link3的soup
print(soup.text) # 打印文本（不包括标签）

#支持CSS选择器
print(soup.select('.story'))
print(soup.select('#link1'))
print(soup.select('p.story'))

soup_lxml = BeautifulSoup(html_doc, 'lxml')
print(soup_lxml.a)