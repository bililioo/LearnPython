# -*- coding: utf-8 -*-

# from sqlalchemy import Column, String, create_engine, ForeignKey, MetaData
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
# import sqlalchemy

# Base = declarative_base()

# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))

#     books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))

#     user_id = Column(String(20), ForeignKey('user.id'))

# engine = create_engine('mysql+mysqlconnector://root:990978664@localhost:3306/test')

# Base.metadata.create_all(engine)

# DBSession = sessionmaker(bind=engine)

# session = DBSession()
# new_user = User(id='3', name='kkk')
# session.add(new_user)
# session.commit()

# user = session.query(User).filter(User.id=='5').one()
# print('type:', type(user))
# print('name:', user.name)

# new_book = Book(id='5', name='A')
# session.add(new_book)
# session.commit()

# session.close()

# -*- coding: utf-8 -*-

# from sqlalchemy import Column, String, create_engine, ForeignKey, MetaData
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = sqlalchemy.Column(sqlalchemy.String(20), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))

    books = sqlalchemy.orm.relationship('Book')

class Book(Base):
    __tablename__ = 'book'

    id = sqlalchemy.Column(sqlalchemy.String(20), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(20))

    user_id = sqlalchemy.Column(sqlalchemy.String(20), sqlalchemy.ForeignKey('user.id'))

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:990978664@localhost:3306/test')

# 建表
# Base.metadata.create_all(engine)

DBSession = sessionmaker(bind=engine)

session = DBSession()
# new_user = User(id='3', name='kkk')
# session.add(new_user)
# session.commit()

user = session.query(User).filter(User.id=='3').one()
print('type:', type(user))
print(user.books[1].name)

# new_book = Book(id='3', name='A')
# session.add(new_book)
# session.commit()

session.close()









