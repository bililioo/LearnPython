#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO
# f = StringIO()
# f.write('hello')
# print(f.getvalue())

f1 = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f1.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f2 = BytesIO()
f2.write('中文'.encode('utf-8'))
print(f2.getvalue())

import os
# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('PATH'))
print(os.path.abspath('.'))

path = os.path.abspath('.')

path1 = os.path.join(path, 'testdir')
# os.mkdir(path1) # 创建testdir文件夹
# os.rmdir(path1) # 删除testdir文件夹

print(os.path.split(path1))
print(os.path.splitext(path1))

print([x for x in os.listdir() if os.path.isdir(x)])
print([x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])



from datetime import datetime

# 打印当前目录的文件信息
pwd = os.path.abspath('.') #绝对路径

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

print('------------------------------------------------------------')

def find_file(name, path=pwd):

    print('current path:', path)
    print('search name: %s \nresults:' % name)

    for p in os.listdir(path):
        if os.path.isdir(p):
            subpath = os.path.join(path, p)
            for root, files in os.walk(subpath):
                for x in files:
                    if name in x:
                        print(os.path.join(root, x))
        elif name in p:
            print(os.path.join(path, p))


# find_file('.db', '/Users/chenbin/Desktop')

import json
d = dict(name='bob', age=20, score=90)
json_str = json.dumps(d)
print(json.loads(json_str))

class Student(object):
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
    
s = Student('bbb', 24, 130)
print(json.dumps(s, default=lambda obj: obj.__dict__))

print(json.loads(json_str, object_hook=dict2student))

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)