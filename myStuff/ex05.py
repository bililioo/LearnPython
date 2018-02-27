# -- coding: utf-8 --

# def odd():
# 	print('step 1')
# 	yield(1)
# 	print('step 2')
# 	yield(3)
# 	print('step 3')
# 	yield(5)

# o = odd()

# for n in o:
# 	print(n)


def triangles():
	L = [1]
	while True:
		yield L 
		for i in range(len(L)):
			print('L = %r' %L)
			print('L[%d - 1] = %d' %(i, L[i - 1]))
			print('L[%d] = %d\n' %(i, L[i]))

		L.append(0)
		L = [L[i - 1] + L[i] for i in range(len(L))]


# t = triangles()
n = 0
for t in triangles():
	print(t)
	n += 1
	if n > 30:
		break

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# n = 0
# results = []
# for t in triangles():
#     print(t)
#     results.append(t)
#     n = n + 1
#     if n == 10:
#         break
# print(results)
# if results == [
#     [1],
#     [1, 1],
#     [1, 2, 1],
#     [1, 3, 3, 1],
#     [1, 4, 6, 4, 1],
#     [1, 5, 10, 10, 5, 1],
#     [1, 6, 15, 20, 15, 6, 1],
#     [1, 7, 21, 35, 35, 21, 7, 1],
#     [1, 8, 28, 56, 70, 56, 28, 8, 1],
#     [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# ]:
#     print('测试通过!')
# else:
#     print('测试失败!')