# -- coding: utf-8 --

from collections import Iterable

# 迭代器
# Iterable 可迭代对象
print(isinstance([], Iterable))

print([x for x in range(10)])

print(isinstance({}, Iterable))

print(abs)

# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# 那么函数名是什么呢？函数名其实就是指向函数的变量！
# 对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
f = abs
print(f(-999))

# 注：由于abs函数实际上是定义在import builtins模块中的，
# 所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

def add(a, b, f):
	return f(a) + f(b)

print(add(-19, -1 , f))

def f(n):
	return n * n

L = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(L))

s = map(str, [1, 2, 3, 4, 5, 6])
print(list(s))

from functools import reduce
def add(x, y):
	return x + y

r = reduce(add, [1, 2, 3])
print(str(r))

r = sum([1, 2, 3, 4])
print(r)

def fn(x, y):
	return x * 10 + y

r = reduce(fn, [1, 2, 3, 4, 5, 6])
print(r)

def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]

k = reduce(fn, map(char2num, '13579'))
print(k)

list1 = map(char2num, '13579')
print(list(list1))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 8, '9': 9, '.': -1}

def str2int(s):
	def fn(x, y):
		return x * 10 + y

	def char2num(s):
		return DIGITS[s]

	return reduce(fn, map(char2num, s))


i = str2int('1231245566')
print(i)

def strToInt(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

print(strToInt('2131244535'))

def normalize(name):
	return name.capitalize()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

def prod(L):
	def multiplication(x, y):
		return x * y
	return reduce(multiplication, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')



CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

def is_odd(s):
	return s % 2 == 1

print(list(filter(is_odd, range(10))))


def not_empty(s):
	return s and s.strip()

print(list(filter(not_empty, ['a', 'b', None, '  '])))


def _odd_iter():
	n = 1
	while True:
		n = n + 2
		yield n

def _not_divisible(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)	


for n in primes():
	if n < 10000:
		print(n)
	else:
		break


def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        return n

output = filter(is_palindrome, range(1, 100))
print(list(output))

# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

sorted([36, 5, -12, 9, -21])
print(sorted([36, 5, -12, 9, -21], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))


from operator import itemgetter


students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=itemgetter(1), reverse=True))

print(sorted(students, key=lambda t: t[1]))





