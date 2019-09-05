# _*_ encoding:utf-8 _*_
__author__: '田敏伦'
__date__: '2019/9/2 0002 19:47'


'''
保存cookie和使用cookie：
    参数：
        ignore_discard：保存即将失效的cookie
    请求发送成功后，将cookie保存到本地：
        cookiejar.save(ignore_discard=True)
    使用cookie：
        cookiejar.load(ignore_discard=True) 
'''


from urllib import request
from http.cookiejar import MozillaCookieJar

# 生成opener
# MozillaCookieJar()有了filename,则save()不需要filename。
cookiejar = MozillaCookieJar('cookies.txt')

# 使用cookie信息
cookiejar.load(ignore_discard=True)  # （在指定文件中[MozillaCookieJar('cookies.txt')]，将cookie加载进来）

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# 发送请求完成后，自动保存cookie到本地。（会自动关闭会话）
resp = opener.open("http://httpbin.org/cookies/set?key=value")

# 使用cookie文件
for i in cookiejar:
    print(i)

# 将cookie保存到本地。
# cookiejar.save(ignore_discard=True)
