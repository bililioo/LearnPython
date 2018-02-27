#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ex09_01

ken = ex09_01.Student('Bart', 66, 'female')

ken.print_score()
print(ken.get_grade())
 
ken.set_score(100)

ken.print_score()
print(ken.get_grade())

# 测试:
bart = ex09_01.Student('Bart', 90, 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

print(type(ken))

import types

print(dir(ex09_01.Student))
print(len(bart))

print(hasattr(bart, 'get_name'))
print(hasattr(bart, 'y'))
setattr(bart, 'y', 19)
print(hasattr(bart, 'y'))
print(getattr(bart, 'y'))



