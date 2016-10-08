from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
import db_controller
import config
import data


app = Flask(__name__)

# HOME ROUTE
@app.route('/')
@app.route('/books')
def showBooksFront():
    category_list = db_controller.get_categories()
    return render_template('front.html',
                            category_list = category_list,
                            recent_books = data.books)


###### CATEGORY ROUTES #####

# ADD A CATEGORY
@app.route('/book/category/add', methods=['GET', 'POST'])
def addBookCategory():
    
    if request.method == "GET":
        return render_template('addBookCategory.html', recent_books = data.books)
    else:
        new_category = db_controller.create_category(request.form['name'])
        return redirect(url_for('showBookCategory', book_cat_id = new_category.id))


# SHOW A CATEGORY
@app.route('/book/category/<int:book_cat_id>')
def showBookCategory(book_cat_id):
    return render_template('showBookCategory.html', 
                            category_list = data.categories, 
                            current_category = data.category,
                            books = data.books)


# EDIT A CATEGORY
@app.route('/book/category/<int:book_cat_id>/edit', methods=['GET', 'POST'])
def editBookCategory(book_cat_id):
    
    if request.method == "GET":
        return render_template('editBookCategory.html',
                                category = data.category)
    else:
        print request.form['name']
        return redirect(url_for('showBookCategory', book_cat_id = data.category['id']))


# DELETE A CATEGORY
@app.route('/book/category/<int:book_cat_id>/delete', methods=['GET', 'POST'])
def deleteBookCategory(book_cat_id):
    
    if request.method == "GET":
        return render_template('deleteBookCategory.html',
                                category = data.category)
    else:
        return redirect(url_for('showBooksFront'))


##### BOOK ROUTES #####

# ADD A BOOK
@app.route('/book/add', methods=['GET', 'POST'])
def addBook():
    if request.method == 'GET':
        return render_template('addBook.html')
    else:
        print request.form['name']
        return redirect(url_for('showBook', book_id = data.book['id']))

# SHOW A BOOK
@app.route('/book/<int:book_id>')
def showBook(book_id):
    return render_template('showBook.html')

# EDIT A BOOK
@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def editBook(book_id):
    if request.method == 'GET':
        return render_template('editBook.html', book = data.book)
    else:
        return redirect(url_for('showBook', book_id = data.book['id']))

# DELETE A BOOK
@app.route('/book/<int:book_id>/delete', methods=['GET', 'POST'])
def deleteBook(book_id):
    if request.method == 'GET':
        return render_template('deleteBook.html', book = data.book)
    else:
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

