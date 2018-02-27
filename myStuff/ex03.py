# -- coding: utf-8 --

import math

# 根据半径求圆面积
def caculate_area(i):
	area = math.pi * i * i
	return area

a = caculate_area(1)
print(a)


print(abs(-111291))

print(max(1, 2, 3, -65, 6, 6.7))

arr = [1, 2, 3, 5, -6]

print(max(arr))

n1 = 255
n2 = 1000

print(hex(n1), hex(n2))

def my_abs(x):
	if not isinstance(x, (int, float)): #类型判断，抛出异常
		raise TypeError('bad operand type')
	if x > 0:	
		return x
	else:
		return -x

print(my_abs(9999))

def nop(str):
	print('%s' %str)
	pass

nop('ff')

# my_abs('fff')

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny #返回是一个tuple

print(move(1, 2, 3))

t = move(1, 2, 3)
print(t[1])

def quadratic(a, b, c):
	if not isinstance(a, int):
		raise TypeError('bad operand type')
				
	x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return x1, x2

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# quadratic(a,f,fc)

def power(num, n=2):
	s = 1
	while n > 0:
		n -= 1
		s = s * num
	return s

print(power(5, 3))
print(power(2))
print(power(2, 2))

def enroll(name, gender, age=6, city='guangzhou'):
	print(name)
	print(gender)
	print(age)
	print(city)

enroll('jffk', 'F', 3)

def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L

print(add_end([1, 2, 3]))
print(add_end([]))


def calc(*number):
	sum = 0 
	for num in number:
		sum = num * num + sum
	return sum

print(calc(*[1, 2, 3]))
print(calc(*(1, 2, 3)))

tempList = (2, 3, 4)
print(calc(*tempList))

print(calc(*()))

def person(name, age, **other):
	# other['city'] = 'fff'
	print('name: %s, age: %s, other: %s' %(name, age, other))

o = {'city': 'guangzhou', 'job': 'engineer'}
person('ben', '24', **o)

o['city'] = 'beijing'
person('ben', '24', **o)

def f1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c,'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f2(1, 2, d=9, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = [1, 2, 3]
f2(*args, **kw)

def product(*numbers):

	if numbers == ():
		return 0

	sum = 1
	for n in numbers:
		sum = sum * n
	return sum

print(product())

# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试成功!')
    except TypeError:
        print('测试失败!')

#递归函数
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
	
print(fact(5))
print(fact(2))
print(fact(100))
# print(fact(1000)) # 栈溢出

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)

print(fact_iter(5, 1))
print(fact_iter(5, 2))


def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')






