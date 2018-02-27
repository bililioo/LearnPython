#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone
import re

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2033, 4, 1, 23, 59, 59)
print(dt)
print(dt.timestamp())

dt_ts = dt.timestamp()

print(datetime.fromtimestamp(dt_ts))

print(now.strftime('%a, %b %Y %d %H:%M'))

t = now + timedelta(hours=20)
print(t)

t = now + timedelta(days=3)
print(t)

t = now + timedelta(days=3, hours=1)
print(t)

tz_utc_8 = timezone(timedelta(hours=8))
now = datetime.now()
print(now)

dt = now.replace(tzinfo=tz_utc_8)
print(dt)

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)

tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

def to_timestamp(dt_str, tz_str):

    r = re.match(r'UTC(\+|\-)(\d{1,2}):(\d{2})', tz_str)
    print(r.group(1))
    print(r.groups())

    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    t = dt
    if r.group(1) == '+':
        t = dt - timedelta(hours=int(r.group(2)))
    elif r.group(1) == '-':
        t = dt + timedelta(hours=int(r.group(2)))
    print(t)
    ts = t.timestamp()
    print(ts)
    return ts


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
# assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
# assert t2 == 1433121030.0, t2

print('ok')