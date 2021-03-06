# -*- coding: utf-8 -*-


# class Query(object):
    
#     def __init__(self, name):
#         self.name =name

#     def __enter__(self):
#         print('Begin')
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
    
#     def query(self):
#         print('Query info about %s...' % self.name)
    

# with Query('bob') as q:
#     q.query()

from contextlib import contextmanager

class Query(object):

    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')

with create_query('bob') as q:
    q.query()

@contextmanager
def tag(name):
    print('<%s>' % name)
    yield
    print('</%s>' % name)

with tag("hi"):
    print('hello')
    

from contextlib import closing
from urllib.request import urlopen

