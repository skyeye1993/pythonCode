from lxml import etree
import requests

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

selector = etree.HTML(html_doc)
# 取出页面内所有的链接
links = selector.xpath('//p[@class="story"]/a/@href')
print(links)

r = requests.get('..../books.xml')  # 见视屏，此处无法运行
se = etree.HTML(r.text)
print(se.xpath('book'))

# 选取书店下所有的书本的作者的名字
print(se.xpath('//bookstore/book/author/text()'))
# 选取书店下所有书本的语言
print(se.xpath('//bookstore/book/title/@lang'))
# 选取书店第一本书的标题
print(se.xpath('//bookstore/book[1]/title/text()'))
# 选取书店最后一本书的标题
print(se.xpath('//bookstore/book[last()]/title/text()'))
# 选取书店最后第二本书的标题
print(se.xpath('//bookstore/book[last()-1]/title/text()'))
# 选取书店前二本书的标题
print(se.xpath('//bookstore/book[position()<3]/title/text()'))
# 选取所有的分类为web的书本
print(se.xpath('//book[@catetory="web"]/title/text()')) # @针对的是标签里面的属性

# 选取所有价格大于35的书本
print(se.xpath('//book[price>35.00]/price/text()'))

#选取所有class属性中包含book的书本的class属性
print('类名中包含book的书本', se.xpath('//book[constains(@class,"book")]/@class/text()'))