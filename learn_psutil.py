# -*- coding: utf-8 -*-

import psutil

print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))

for x in range(10):
    print(psutil.cpu_times())

print(psutil.virtual_memory())
print(psutil.swap_memory())

print(psutil.disk_partitions())