from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
import db_controller
import config


app = Flask(__name__)


# HOME ROUTE
@app.route('/')
@app.route('/books')
def showBooksFront():
    category_list = db_controller.get_categories()
    books = db_controller.get_recent_books(5)
    return render_template('front.html',category_list = category_list,
                            recent_books = books)

###### CATEGORY ROUTES #####

# ADD A CATEGORY
@app.route('/book/category/add', methods=['GET', 'POST'])
def addBookCategory():
    if request.method == "GET":
        return render_template('addBookCategory.html')
    else:
        new_category = db_controller.create_category(request.form['name'])
        return redirect(url_for('showBookCategory', book_cat_id = new_category.id))


# SHOW A CATEGORY
@app.route('/book/category/<int:book_cat_id>')
def showBookCategory(book_cat_id):
    categories = db_controller.get_categories()
    current_category = db_controller.get_category(book_cat_id)
    books = db_controller.get_books_by_category(book_cat_id)
    return render_template('showBookCategory.html', 
                            category_list = categories, 
                            current_category = current_category,
                            books = books)

# EDIT A CATEGORY
@app.route('/book/category/<int:book_cat_id>/edit', methods=['GET', 'POST'])
def editBookCategory(book_cat_id):
    category = db_controller.get_category(book_cat_id)
    
    if request.method == 'GET':
        return render_template('editBookCategory.html',
                                category = category)
    if request.method == 'POST':
        category = db_controller.update_category(id = category.id, 
                                                 name = request.form['name'])
        return redirect(url_for('showBookCategory', book_cat_id = category.id))


# DELETE A CATEGORY
@app.route('/book/category/<int:book_cat_id>/delete', methods=['GET', 'POST'])
def deleteBookCategory(book_cat_id):
    category = db_controller.get_category(book_cat_id)
    
    if request.method == "GET":
        return render_template('deleteBookCategory.html',
                                category = category)
    else:
        db_controller.delete_category(category.id)
        return redirect(url_for('showBooksFront'))


##### BOOK ROUTES #####

# ADD A BOOK
@app.route('/book/add', methods=['GET', 'POST'])
def addBook():
    categories = db_controller.get_categories()
    
    if request.method == 'GET':
        return render_template('addBook.html', categories = categories)
    if request.method == 'POST':
        book = db_controller.create_book(
            name = request.form['name'],
            author = request.form['author'],
            description = request.form['description'],
            price = request.form['price'],
            image = request.form['image'],
            category_id = request.form['category'],
            # TODO: Need to set user id to login_session['user_id'] when system is created
            user_id = 1)
        return redirect(url_for('showBook', book_id = book.id))

# SHOW A BOOK
@app.route('/book/<int:book_id>')
def showBook(book_id):
    book = db_controller.get_book(book_id)
    return render_template('showBook.html', book = book)

# EDIT A BOOK
@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def editBook(book_id):
    categories = db_controller.get_categories()
    book = db_controller.get_book(book_id)
    
    if request.method == 'GET':
        return render_template('editBook.html', book = book, categories = categories)
    if request.method == 'POST':
        print request.form['category']
        print request.form['name']
        book = db_controller.update_book(
            book_id = book.id,
            name = request.form['name'],
            author = request.form['author'],
            description = request.form['description'],
            price = request.form['price'],
            image = request.form['image'],
            category_id = request.form['category'])
        return redirect(url_for('showBook', book_id = book.id))

# DELETE A BOOK
@app.route('/book/<int:book_id>/delete', methods=['GET', 'POST'])
def deleteBook(book_id):
    book = db_controller.get_book(book_id)
    
    if request.method == 'GET':
        return render_template('deleteBook.html', book = book)
    if request.method == 'POST':
        book = db_controller.delete_book(book.id)
        return redirect(url_for('showBooksFront'))

##### ADMIN ROUTES #####
@app.route('/admin')
def adminMain():
    users = db_controller.get_users()
    categories = db_controller.get_categories()
    books = db_controller.get_books()
    return render_template('admin.html', users = users, categories = categories, books = books)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = config.secret_key
    app.run(config.host, config.port)

