# -*- coding: utf-8 -*-

import itertools

# natuals = itertools.count(1)
# for n in natuals:
#     print(n)

# cs = itertools.cycle('abc')
# for c in cs:
#     print(c)


ns = itertools.repeat('afc', 3)
for n in ns:
    print(n)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

for c in itertools.chain('ABC', 'XYZ'):
    print(c)
# 迭代效果：'A' 'B' 'C' 'X' 'Y' 'Z' 

for key, group in itertools.groupby('AAABBBCCVVAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

# def pi(N):
#     ' 计算pi的值 '
#     # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
#     odds = itertools.count(1,2)

#     # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
#     odds = itertools.takewhile(lambda x: x <= 2 * N - 1, odds)

#     # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
#     L = [(4/x) * (-1) ** ((x -1) / 2) for x in list(odds)]

#     # step 4: 求和:
#     return sum(L)

from functools import reduce

from datetime import datetime

def pi(n):
    js=itertools.takewhile(lambda x:x<=2*n-1, itertools.count(1, 2))
    r = reduce(lambda x,y:x+y, map(lambda x: (4/x) if ((x-1)/2) % 2 == 0 else (-4/x), js))
    return r
    

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
