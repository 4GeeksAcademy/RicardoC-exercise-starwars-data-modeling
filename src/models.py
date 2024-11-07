import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, primary_key=True) 
    username = Column(String(25), nullable=False)
    firstname = Column(String(25), nullable=False)
    lastname = Column(String(25), nullable=False)
    email = Column(String, unique=True, nullable=False) 
    password = Column(String, nullable=False)
    favorites_characters = relationship('Favorites_Character', back_populates='user')
    favorites_planets = relationship('Favorites_Planet', back_populates='user')
    favorites_vehicles = relationship('Favorites_Vehicle', back_populates='user')

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(25))
    gender = Column(String(10))
    birthday_year = Column(Integer)
    favorites_character = relationship('Favorites_Character', back_populates='character')

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(15))
    climate = Column(String(15))
    population = Column(String(15))
    favorites_planet = relationship('Favorites_Planet', back_populates='planet')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_key=True)
    name = Column(String(15))
    model = Column(String(15))
    manufacturer = Column(String(15))
    favorites_vehicle = relationship('Favorites_Vehicle', back_populates='vehicle')

class Favorites_Character(Base):
    __tablename__ = 'favorites_character'
    character_favorites_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    character_id = Column(Integer, ForeignKey('character.character_id'))
    user = relationship('User', back_populates='favorites_characters')
    character = relationship('Character', back_populates='favorites_character')

class Favorites_Planet(Base):
    __tablename__ = 'favorites_planet'
    favorite_planet_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    user = relationship('User', back_populates='favorites_planets')
    planet = relationship('Planet', back_populates='favorites_planet')

class Favorites_Vehicle(Base):
    __tablename__ = 'favorites_vehicle'
    favorite_vehicle_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'))
    user = relationship('User', back_populates='favorites_vehicles')
    vehicle = relationship('Vehicle', back_populates='favorites_vehicle')








    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
