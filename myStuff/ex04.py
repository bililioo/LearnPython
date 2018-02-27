# -- coding: utf-8 --
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 切片	
print(L[0:3])
print(L[:3])

L2 = list(range(100))
print(L2[:10:3])
print(L2[::3])

print(L2[9:-2])

def trim(s):
	print('输入的内容(%s)' %s)

	if s == '':
		print('最终结果：%s' %s)
		return s

	if s[0] == ' ':
		s = s[1:]
		print('前空格', s)
		return trim(s)

	if s[-1] == ' ':
		s = s[0:-1]
		print('后空格', s)
		return trim(s)

	print('最终结果：%s' %s)
	return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
	print(key)

for value in d.values():
	print(value)

for key, value in d.items():
	print(key, value)

# 迭代
from collections import Iterable

print(isinstance('abc', Iterable)) # str是否可迭代
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

for i, value in enumerate(L):
	print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)

def findMinAndMax(L):
	if L == []:
		max = None
		min = None
	else: 
		max = L[0]
		min = L[0]
		for i in L:
			if i > max:
				max = i
			if i < min:
				min = i

	return (min, max)			


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
    
# 列表生成式
print([x * x for x in range(1, 10)])

t = [m + n for m in 'ABCDEFG' for n in 'XYZ']
print(t)

import os # 导入os模块，模块的概念后面讲到
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])

L2 = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L2])

L3 = ['Hello', 'World', 18, 'Apple', None]

L4 = [s.lower() for s in L3 if isinstance(s, str)]

print(L4)
if L4 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

# 生成器
g = (x * x for x in range(1, 10))
print(g)

for n in g:
	print(n)

def fib(max):
	n, a, b = 0, 0, 1
	while  n < max:
		# print(b)
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'

print(fib(10))

f = fib(10)
for n in f:
	print(n)

def odd():
	print('step 1')
	yield(1)
	print('step 2')
	yield(3)
	print('step 3')
	yield(5)










