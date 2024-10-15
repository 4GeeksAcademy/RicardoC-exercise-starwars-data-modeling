import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base): 
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True )
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String,unique=True, nullable=False)
    password = Column(String, nullable=False)
    User_Character = relationship('Favorites_Character')


class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name =  Column(String(25))
    gender = Column(String(10))
    birthday_year = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    favorites_Character = relationship('Favorites_Character')

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_Key= True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    name = Column(String(15))
    climate = (String(15))
    population = (String(15))

class Favorites_Character(Base):
    __tablename__ = 'favorites_character'
    character_Favorites_id = Column(Integer, primary_Key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character_relationship = relationship(Character)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_Key= True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user_relationship = relationship(User)
    name = Column(String(15))
    model = Column(String(15))
    manufacturer = Column(String(15))








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
