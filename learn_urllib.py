# -*- coding: utf-8 -*-

from urllib import request, parse
import ssl
import json

# with request.urlopen('https://api.douban.com/v2/book/2129650', context=ssl._create_unverified_context()) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/11.0 Mobile/10A5376e Safari/8536.25')

# with request.urlopen(req, context=ssl._create_unverified_context()) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))


class Data(object):
    def __init__(self, retcode, msg, data):
        self.retcode = retcode
        self.msg = msg
        self.data = data

d = Data('','','')
print(dir(d))
print(d.__dict__)

# def dict2data(d):
#     return Data(d['retcode'], d['msg'], d['data'])

def MyJsonLoads(cls, jsonStr):
    clsDict = cls.__dict__
    jsonDict = json.loads(jsonStr)
    className = str(type(cls))[str(type(cls)).find('.') + 1:-2]
    newObj = eval(className + '()')
    for key in clsDict:
        setattr(newObj, key, jsonDict[key])
    return newObj

print('Login to weibo.cn...')
email = '13622746432'
passwd = 'Bunchan16'
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8'), context=ssl._create_unverified_context()) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    # print('Data:', f.read().decode('utf-8'))

    json_str = f.read().decode('utf-8')
    s = MyJsonLoads(Data('','',''), json_str)
