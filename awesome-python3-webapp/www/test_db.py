# -*- coding: utf-8 -*-

import asyncio
import orm
from models import User, Blog, Comment

async def test_db(loop):
    await orm.create_pool(loop=loop, host='127.0.0.1', user='root', password='990978664', db='awesome')

    # u = User(name='Ben', email='schuamcher23@qq.com', password='123456', image='about:blank', admin=1)
    # await u.save()

    u1 = User(name='James', email='fake@qq.com', password='123456', image='about:blank', admin=0)
    await u1.save()

    u = await User.findAll()
    print(u)

loop = asyncio.get_event_loop()
loop.run_until_complete(test_db(loop))
# loop.run_forever()

