import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    eye_color = Column(String(120), nullable=False)
    hair_color = Column(String(120), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)
    ships_id = Column(Integer, ForeignKey('ships.id'),
        nullable=False)    
    favoritos = relationship('fav', backref='characters', lazy=True)


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)


class Ships(Base):
    __tablename__ = 'ships'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    model = Column(String(80), nullable=False)
    planets_id = Column(Integer, ForeignKey('planets.id'),
        nullable=False)    
    



class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    population = Column(Integer, nullable=False)    
    characters = relationship('characters', backref='planets', lazy=True)
    ships = relationship('ships', backref='planets', lazy=True)



class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'),
        nullable=False)

    def to_dict(self):
        return {}



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')