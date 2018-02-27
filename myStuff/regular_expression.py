#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))

print(re.match(r'^\d{3}\-\d{3,8}$', '010 12345'))

test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

test_str = 'a, b, ;;   c d'

t = test_str.split(' ')
print(t)

t = re.split(r'\s+', test_str)
print(t)

t = re.split(r'[\s\,]+', test_str)
print(t)

t = re.split(r'[\s\,\;]+', test_str)
print(t)

print('============================')

def is_valid_email(addr):

    r = re.match(r'(\w+)\.?(\w+)@(\w+\.com)', addr)
    print('@@@@@@@', r)
    if r != None:
        print(r.groups())
        return True
    return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')