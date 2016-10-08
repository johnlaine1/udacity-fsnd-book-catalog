from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Category, Book

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# CATEGORY RELATED FUNCTIONS
def get_categories():
	categories = session.query(Category).all()
	return categories

def create_category(name):
	category = Category(name = name)
	session.add(category)
	session.commit()
	return category

def get_category(id):
	category = session.query(Category).filter_by(id == id).one()
	return category

def update_category(id, name):
	category = get_category(id)
	category.name = name
	session.add(category)
	session.commit()
	return category

def delete_category(id):
	category = get_category(id)
	session.delete(category)
	session.commit()
	return category

# BOOK RELATED FUNCTIONS
def get_books_by_category(category_id):
	books = session.query(Book).filter_by(category_id = category_id).all()
	return books

def get_book(book_id):
	book = session.query(Book).filter_by(id = book_id).one()
	return book

def create_book(name, description, price, image, category_id):
	book = Book(name = name, description = description, price = price, image = image, category_id = category_id)
	session.add(book)
	session.commit()
	return book

def update_book(book_id, name, description, price, image):
	book = get_book(book_id)
	book.name = name
	book.description = description
	book.price = price
	book.image = image
	session.add(book)
	session.commit()
	return book

def delete_book(book_id):
	book = session.query(Book).filter_by(id = book_id).one()
	session.delete(book)
	session.commit()
	return book