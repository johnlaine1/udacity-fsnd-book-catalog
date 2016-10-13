from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Book

# Connect to DB and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

##### CATEGORY RELATED FUNCTIONS #####

def create_category(name):
	"""Creates a single category.

	Args:
		name: (string)The name of the category

	Returns:
		The newly created category
	"""

	category = Category(name = name)
	session.add(category)
	session.commit()
	return category

def create_categories(categories):
	"""Creates multiple categories

	Args:
		categories: A list of dictionaries formatted as:
			{'name': 'CATEGORY_NAME'}
	"""

	for category in categories:
		create_category(**category)

def get_category(id):
	"""Returns a single category object

	Args:
		id: (int) The ID of the category to retrieve

	Returns:
		The category object requested
	"""

	category = session.query(Category).filter_by(id = id).one()
	return category

def get_categories():
	"""Returns all categories in the database"""

	categories = session.query(Category).all()
	return categories

def update_category(id, name):
	"""Updates a category in the database"""

	category = get_category(id)
	category.name = name
	session.add(category)
	session.commit()
	return category

def delete_category(id):
	"""Deletes a category from the database"""

	category = get_category(id)
	session.delete(category)
	session.commit()
	return category

def category_exists(name):
	"""Returns a category object if it exists, else None"""

	try:
		category = session.query(Category).filter(func.lower(Category.name) == func.lower(name)).all()
	except:
		category = None

	return category

##### BOOK RELATED FUNCTIONS #####

def create_book(name, author, description, price, image, category_id, user_id):
	"""Create an individual book in the database"""

	book = Book(name = name, author = author, description = description,
				price = price, image = image, category_id = category_id,
				user_id = user_id)
	session.add(book)
	session.commit()
	return book

def create_books(books):
	"""Create multiple books in the database"""

	for book in books:
		create_book(**book)

def get_book(book_id):
	"""Get an individual book from the database"""

	book = session.query(Book).filter_by(id = book_id).one()
	return book

def get_books():
	"""Get multiple books from the database"""

	books = session.query(Book).all()
	return books

def get_books_by_category(category_id):
	"""Get all books that belong to a certain category"""

	books = session.query(Book).filter_by(category_id = category_id).all()
	return books

def get_recent_books(num):
	"""Get the most recent books created"""

	try:
		books = session.query(Book).order_by(desc(Book.created)).limit(num).all()
	except:
		books = None
	return books

def update_book(book_id, name, author, description, price, image, category_id):
	"""Update a book in the database"""

	book = get_book(book_id)
	book.name = name
	book.description = description
	book.price = price
	book.image = image
	book.category_id = category_id
	session.add(book)
	session.commit()
	return book

def delete_book(book_id):
	"""Delete a book from the database"""

	book = session.query(Book).filter_by(id = book_id).one()
	session.delete(book)
	session.commit()
	return book

##### USER RELATED FUNCTIONS #####

def create_user_from_session(login_session):
	"""Create a user from session data"""

	newUser = User(name = login_session['username'],
	        	   email = login_session['email'],
	        	   picture = login_session['picture'])
	session.add(newUser)
	session.commit()
	user = session.query(User).filter_by(email = login_session['email']).one()
	return user.id

def create_user(name, email = '', picture = '', role = ''):
	"""Create a new user in the database"""

	user = User(name = name, email = email, picture = picture, role = role)
	session.add(user)
	session.commit()
	return user

def create_users(users):
	"""Create multiple users in the database"""

	for user in users:
		create_user(**user)

def get_user(user_id):
	"""Get a user from the database"""

	user = session.query(User).filter_by(id = user_id).one()
	return user

def get_users():
	"""Get multiple users from the database"""

	users = session.query(User).all()
	return users

def get_user_id_from_email(email):
	"""Get a user ID based on the users email address"""

	try:
		user = session.query(User).filter_by(email = email).one()
		return user.id
	except:
		return None

def update_user(user_id, name, email, picture, role):
	"""Update an existing user in the database"""

	user = get_user(user_id)
	user.name = name
	user.email = email
	user.picture = picture
	user.role = role
	session.add(user)
	session.commit()
	return user

def delete_user(user_id):
	"""Delete a user from the database"""
	user = get_user(user_id)
	session.delete(user)
	session.commit()
	return user