from bs4 import BeautifulSoup
import requests
import os
import urllib

r = requests.get('http://www.xiachufang.com',headers={'User-Agent': 'Custom'})
soup = BeautifulSoup(r.text)

img_list = []
for img in soup.select('img'):
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])

# 初始化下载文件目录
image_dir = os.path.join(os.curdir,'images')
if not os.path.isdir(image_dir):
    os.mkdir(image_dir)

for img in img_list:
    o = urllib.parse.urlparse(img)
    filepath = os.path.join(image_dir, o.path[1:])
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))
    url = '%s://%s%s' % (o.scheme, o.netloc, o.path)
    print(url)
    resp = requests.get(url)
    with open(filepath, 'wb') as f:
        for chunk in resp.iter_content(1024):
            f.write(chunk)
