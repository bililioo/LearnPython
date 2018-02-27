# -- coding: utf-8 --
# List
templist = ['michael', 'ben', 'bash', 'shell']

print(len(templist))

print(templist[0])
print(templist[-1])	

templist.append('iOS')
print(templist)

templist.insert(1, 'schumacher')
print(templist)

templist.pop()
print(templist)

templist.pop(0)
print(templist)

templist[1] = 'chan'
print(templist)


tempList2 = ['what', 3.124, False, templist]
print(tempList2)
print(tempList2[-1][-1])


# Tuple
tempTuple = (1, 2, "kfc", templist)
print(tempTuple)

templist.pop()
print(tempTuple)

tempTuple1 = (1,)
print(tempTuple1)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[-1][-1])	

age = 11
if age > 19:
	print("ahhhh")
elif age == 11:
	print(age)
else:
	print('nononono')

a = 1

if a:
	print(True)
else:
	print(False)

height = 1.70
weight = 60

bmi = weight / (height * height)
print(bmi)
if bmi < 18.5:
	print('过轻')
elif bmi <= 25:
	print('正常')
elif bmi <= 28:
	print('过重')
elif bmi <= 32:
	print('肥胖')
else:
	print('严重肥胖')

	
names = ['michael', 'ben', 'chan']
for name in names:
	print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(range(5))	
print(list(range(5)))

sum2 = 0
for x in range(101):
	sum2 += x
print(sum2)


sum3 = 0
n = 99
while n > 0:
	sum3 += n
	n -=2
print(sum3)

L2 = ['Bart', 'Lisa', 'Adam']
for name in L2:
	print('hello %s!' %name)


n = 0
while  n < 100:	
	print(n)
	n += 3
	if n > 37:
		break

m = 0
while m < 10:
	m +=1
	if m % 2 == 0:
		continue
	print(m)

dict1 = {'ben': 99, 'michael': 98, 'chan': 97}
print(dict1['ben'])
dict1['bin'] = 101
print(dict1)

print('ben' in dict1)
print('alonso' in dict1)

print(dict1.get('ben'))

dict1.pop('ben')
print(dict1)

s = set([1, 2, 3, 3, 3, 4, 4, 5])
print(s)
s.add(121)
print(s)
s.remove(121)
print(s)

s1 = set([0, 1, 2, 3, 4, 5, 6])
print(s1 & s)
print(s1 | s)

arr = ['c', 'b', 'a']
arr.sort()
print(arr)

str = "string"
str = str.replace('s', 'S')
print(str)

a = 'abc'
a = a.replace('a', 'A')
print(a)


