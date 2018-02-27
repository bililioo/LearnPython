# -*- coding: utf-8 -*-

import sqlite3
import os
# # 连接到SQLite数据库
# # 数据库文件是test.db
# # 如果文件不存在，会自动在当前目录创建:
# conn = sqlite3.connect('test.db')
# # 创建一个Cursor:
# cursor = conn.cursor()
# # 执行一条SQL语句，创建user表:
# # cursor.execute('CREATE TABLE user (id varchar(20) primary key, name varchar(20))')
# # 继续执行一条SQL语句，插入一条记录:
# cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
# cursor.execute('insert into user (id, name) values (\'2\', \'fds\')')

# # 通过rowcount获得插入的行数:
# print(cursor.rowcount)
# # 关闭Cursor:
# cursor.close()
# # 提交事务:
# conn.commit()
# # 关闭Connection:
# conn.close()




# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# cursor.execute('select * from user where id=?', ('1',))

# values = cursor.fetchall()
# print(values)

# cursor.close()
# conn.close()

import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    # ' 返回指定分数区间的名字，按分数从低到高排序 '
    pass
    
# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')