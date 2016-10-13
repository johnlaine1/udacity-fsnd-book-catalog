from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime, timedelta
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    created = Column(DateTime, default=datetime.utcnow)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))
    role = Column(String(250))
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'        : self.id,
            'created'   : self.created,
            'name'      : self.name,
            'email'     : self.email,
            'picture'   : self.picture,
            'role'      : self.role
        }
    
    
class Category(Base):
    __tablename__ = 'category'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id'    : self.id,
            'name'  : self.name
        }


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key = True)
    created = Column(DateTime, default=datetime.utcnow)
    name =Column(String(80), nullable = False)
    author = Column(String(80))
    description = Column(String(250))
    price = Column(String(8))
    image = Column(String(250))
    category_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'id'         : self.id,
           'created'    : self.created,
           'name'       : self.name,
           'author'     : self.author,
           'description': self.description,
           'price'      : self.price,
           'image'      : self.image,
           'category'   : self.category.name,
           'user'       : self.user.name
       }

engine = create_engine('sqlite:///catalog.db')

Base.metadata.create_all(engine)
