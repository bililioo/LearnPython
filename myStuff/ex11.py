#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdb

try:
	print('try...')
	# r = 10 / int('a')
	r = 10 / 0
	print(r)
except ValueError as error:
	print('except:', error)
except ZeroDivisionError as error:
	print('except:', error)
else:
	print('no error')
finally:
	print('finally')
print('END')


# def foo():
#     r = some_function()
#     if r==(-1):
#         return (-1)
#     # do something
#     return r

# def some_function():
# 	return 11

# def bar():
#     r = foo()
#     if r==(-1):
#         print('Error')
#     else:
#         pass

# try:
# 	foo()
# except ValueError as error:
# 	print('ValueError')
# except UnicodeError as error:
# 	print('UnicodeError')

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	# bar('0')
	try:
		bar('0')
	except Exception as e:
		print('error:', e)
	else:
		pass
	finally:
		print('finally')


main()

pdb.set_trace()
def fn1(s):
	n = int(s)
	assert n != 0, 'n is zero!!!!'
	return 10 / n

# fn1(0)

import logging

logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)







