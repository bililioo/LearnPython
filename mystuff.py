# -*- coding: utf-8 -*-

from contextlib import closing
from urllib.request import urlopen
import ssl

print('ffff')

with closing(urlopen('http://www.baidu.com')) as page:
    for line in page:
        print(line)


