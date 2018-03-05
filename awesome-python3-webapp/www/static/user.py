# -*- coding:utf-8 -*-

from orm import Model, StringField, IntegerField

class User(Model):
    __table = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()


user = User(id=123, name='Ben')
user.save()

user = User(id=12, name='ben')
user.save()


# user.insert()
# user = await User.find('123')
# users = User.findAll()