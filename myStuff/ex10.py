#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

	__slots__ = ('name', 'age')



s = Student
s.name = 'Michael'
print(s.name)

def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age = 24

s.score = 100
print(s.score)


class Screen(object):
    
	@property
	def height(self):
		return self._height

	@property
	def width(self):
		return self._width

	@property
	def resolution(self):
		self._resolution = 786432
		return self._resolution

	@width.setter
	def width(self, value):
		self._width = value

	@height.setter
	def height(self, value):
		self._height = value



# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Teacher(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Teacher('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')


class Hello(object):

	def hello(self, name='world'):
		print('hello, %s' % name)


h = Hello()
h.hello()
print(type(Hello))
print(type(h))

def function(self, name='world'):
	print('hello, %s' % name)

Halo = type('Halo', (object,), dict(halo=function))
h1 = Halo()
h1.halo()




