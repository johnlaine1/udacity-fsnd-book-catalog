from sqlalchemy import create_engine, desc, func
from sqlalchemy.orm import sessionmaker
from db_setup import Base, User, Category, Book

# Connect to DB and creat database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# CATEGORY RELATED FUNCTIONS

def create_category(name):
	category = Category(name = name)
	session.add(category)
	session.commit()
	return category
	
def create_categories(categories):
    for category in categories:
        create_category(**category)

def get_category(id):
	category = session.query(Category).filter_by(id = id).one()
	return category

def get_categories():
	categories = session.query(Category).all()
	return categories
	
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

def category_exists(name):
	try:
		category = session.query(Category).filter(func.lower(Category.name) == func.lower(name)).all()
	except:
		category = None
		
	return category
	
# BOOK RELATED FUNCTIONS

def create_book(name, author, description, price, image, category_id, user_id):
	book = Book(name = name, author = author, description = description, 
				price = price, image = image, category_id = category_id,
				user_id = user_id)
	session.add(book)
	session.commit()
	return book

def create_books(books):
    for book in books:
        create_book(**book)
        
def get_book(book_id):
	book = session.query(Book).filter_by(id = book_id).one()
	return book
	
def get_books():
	books = session.query(Book).all()
	return books
	
def get_books_by_category(category_id):
	books = session.query(Book).filter_by(category_id = category_id).all()
	return books
        
def get_recent_books(num):
	books = session.query(Book).order_by(desc(Book.created)).limit(num)
	return books
	
	
def update_book(book_id, name, author, description, price, image, category_id):
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
	book = session.query(Book).filter_by(id = book_id).one()
	session.delete(book)
	session.commit()
	return book
	
# USER RELATED FUNCTIONS
def create_user_from_session(login_session):
	  newUser = User(name = login_session['username'],
	             email = login_session['email'],
	             picture = login_session['picture'])
	  session.add(newUser)
	  session.commit()
	  user = session.query(User).filter_by(email = login_session['email']).one()
	  return user.id
	  
def create_user(name, email = '', picture = '', role = ''):
	user = User(name = name, email = email, picture = picture, role = role)
	session.add(user)
	session.commit()
	return user

def create_users(users):
    for user in users:
		create_user(**user)
        
def get_user(user_id):
	user = session.query(User).filter_by(id = user_id).one()
	return user
	
def get_users():
	users = session.query(User).all()
	return users
	
def get_user_id_from_email(email):
	try:
		user = session.query(User).filter_by(email = email).one()
		return user.id
	except:
		return None
		
def update_user(user_id, name, email, picture, role):
	user = get_user(user_id)
	user.name = name
	user.email = email
	user.picture = picture
	user.role = role
	session.add(user)
	session.commit()
	return user

def delete_user(user_id):
	user = get_user(user_id)
	session.delete(user)
	session.commit()
	return user