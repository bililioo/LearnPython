# -- coding: utf-8 --

def log(func):
	def wrapper(*args, **kw):
		print('call %s():' %func.__name__)
		return func(*args, **kw)
	return wrapper

def calc_sum(*args):
	ax = 0
	for n in args:
		ax = ax + n
	return ax

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1, 2, 3)
print(f)
print(f())

def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 5):
		fs.append(f(i))
	return fs

f1, f2, f3, f4 = count()
print(f1(), f2(), f3(), f4())

def createCounter():
    f = [0]
    print('闭包外--')
    def counter():
        print('闭包内--')
        f[0] += 1
        return f[0]
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

# array 可以改变元素
a = [0, 2, 3]
a[0] += 1
print(a)

# tuple 不能改变元素
# b = (1, 2, 3)
# b[0] += 1
# print(b)

f = lambda x : x + 1024
print(f(5))

def build(x, y):
	return lambda: x + y
print(build(10, 10)())

def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
print(L)

L1 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L1)

@log
def now():
	print('2018年02月06日14:51:55')

n = now
n()

print(now.__name__)
print(n.__name__)

@log
def now2():
	print('2018-02-06 15:35:39')

now2()
now()

import time, functools

def metric(func):
	def wrapper(*args, **kw):
		start = time.time()
		function = func(*args, **kw)
		end = time.time()
		print('%s executed in %.10s ms' % (func.__name__,  end - start))
		return function
	return wrapper

# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')



















