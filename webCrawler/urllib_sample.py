import urllib.request
import json

r = urllib.request.urlopen('http://httpbin.org/get')
print(dir(r))
# 读取response的内容
text = r.read()
# http返回状态码和msg
print(r.status, r.reason)
obj = json.loads(text)
print(obj)

# r.headers是一个HTTPMessage对象
# print(r.headers)
for k, v in r.headers._headers:
    print('%s : %s ' % (k, v))

# 使用GET参数
params = urllib.parse.urlencode({'spam': 1, 'eggs': 2, 'bacon': 3})
url = 'http://httpbin.org/get?%s' % params
with urllib.request.urlopen(url) as f:
    print(json.load(f))

# 使用POST方法传递参数
data = urllib.parse.urlencode({'name':'zhangsan', 'age':'123'})
data = data.encode()
with urllib.request.urlopen('http://httpbin.org/post', data) as f:
    print(json.load(f))

o = urllib.parse.urlparse('http://zhangsan:123@httpbin.org/get?a=1&b=2#test')
print(o.netloc)
print(o.path)
print(o.query)
print(o.fragment)
print(o.geturl())
print(list(o))