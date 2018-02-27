#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

en_str = base64.b64encode(b'binary\x00string')
print(en_str)

de_str = base64.b64decode(en_str)
print(de_str)

en_str = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(en_str)

de_str = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(de_str)

print('------------------------')

def safe_base64_decode(s):
    last = s[-2:]
    b = s
    if last != b'==': 
        temp_str = s.decode() + '=='
        b = temp_str.encode()

    return base64.b64decode(b)
        
    
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')