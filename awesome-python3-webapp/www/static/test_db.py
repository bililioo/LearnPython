# -*- coding: utf-8 -*-

import asyncio
import orm
from models import User, Blog, Comment

async def test_db(loop):
    await orm.create_pool(user='root', pwd='990978664', db='awesome', loop=loop)
    # u = User(name='Test', email='test@example.com', password='1234567890', image='about:blank')
    # await u.save()

    u = User(name='Ben', email='schuamcher23@qq.com', pwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_db(loop))
loop.run_forever()

