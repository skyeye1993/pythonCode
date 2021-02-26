import requests

# GET请求
r = requests.get('http://httpbin.org/get')
print(r.status_code, r.reason)
print(r.text)
# 带参数的GET请求
r = requests.get('http://httpbin.org/get', params={'a': 1, 'b': 2})
print(r.json())

# POST请求
r = requests.post('http://httpbin.org/post', data={'a': 1})
print(r.json())

# 自定义的headers请求
ua = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
     '(KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
headers = {'User-Agent': ua}
r = requests.get('http://httpbin.org/headers', headers=headers)
print(r.json())

# 带cookies的请求
cookies = dict(userid='123456', token='xxx')
r = requests.get('http://httpbin.org/cookies', cookies = cookies)
print(r.json())

# Basic-auth认证请求
r = requests.get('http://httpbin.org/basic-auth/zhangsan/123456', auth = ('zhangsan', '123456'))
print(r.json())

# 主动抛出状态码异常
bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
# bad_r.raise_for_status() # 主动抛出异常

# 获取session中的cookies
s = requests.Session()
s.get('http://httpbin.org/cookies/set/userid/123456')
r = s.get('http://httpbin.org/cookies')
print(r.json())

r = requests.get('http://httpbin.org/delay/4', timeout=5)
print(r.json())