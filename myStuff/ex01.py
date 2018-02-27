# -- coding: utf-8 --
# print("hello world!");
# print("广州!");

print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)
print(3 + 2 < 5 -7)
print(3 + 2 + 1 - 5 + 4 % 2 -1 / 4 + 6)

print("int(3.14159 + 3.14) =", int(3.14159 + 3.14))
print("float(3.14159 + 3.14) =", float(3.14159 + 3.14))

cars = 100
space_in_a_car = 4.0
dirvers = 30
passengers = 90
cars_not_driven = cars - dirvers
cars_driven = dirvers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("there are", cars, "cars available")
print("there are", dirvers, "dirvers available")

my_name = 'ben'
my_inches = 74
print("my name is %s." %my_name)
print("I'm %d inches tall." %my_inches)

variable = 'wasd'
print ("这是一个万能格式化字符: %r")

i = "i"
a = 4

print("%s = %a" %(i, a))
print(i + i)

formatter = "%r %r %r %r"
print(formatter %(2, 4, 6, 8))
print(formatter %('f', 'u', 'c', 'k'))

# print("how old are you?"),
# age = input("age = ")
# print("you age %s" %age)

# anwser = input("how are you?")
# print(anwser)

# 导入sys库里的argv
# from sys import argv
import sys

# script = sys.argv[0]
# first = sys.argv[1]
# second = sys.argv[2]
# third = sys.argv[3]

# print("the script is called:", script)
# print("your first variable is:", first)
# print("your second variable is:", second)
# print("your third variable is:", third)

prompt = '> '

# user_name = input(prompt)

# print("hi %s" %user_name)

# script = sys.argv[0]
# file_name = sys.argv[1]


file_name = "test01.txt"

# txt = open(file_name,'w')
txt = open(file_name, 'w')

# original = txt.read()
# print(original)

append_string = "2018年01月18日17:53:47"
print(append_string)
txt.write("append_string")

txt.close()

print('''line1
	line21
line3''')

print(ord("中"))
print('ABC'.encode('ascii'))

chinese = '中文'.encode('utf-8')
print(chinese)

utf8 = chinese.decode('utf-8', errors='ignore')
print(utf8)

print(len(utf8))
print(len(chinese))

s1 = 72
s2 = 85
r = (s2 - s1) / s1
r = r * 100
print('%.1f%%' %r)