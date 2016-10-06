from flask import Flask, render_template, request
from flask import session as login_session
import config


app = Flask(__name__)


# HOME ROUTE
@app.route('/')
@app.route('/books')
def showBooks():
    return render_template('front.html')


# CATEGORY ROUTES
@app.route('/book/category/add')
def addBookCategory():
    return render_template('addBookCategory.html')


@app.route('/book/category/<int:book_cat_id>')
def showBookCategory(book_cat_id):
    return render_template('showBookCategory.html')


@app.route('/book/category/<int:book_cat_id>/edit')
def editBookCategory(book_cat_id):
    return render_template('editBookCategory.html')


@app.route('/book/category/<int:book_cat_id>/delete')
def deleteBookCategory(book_cat_id):
    return render_template('deleteBookCategory.html')


# BOOK ROUTES
@app.route('/book/add')
def addBook():
    return render_template('addBook.html')


@app.route('/book/<int:book_id>')
def showBook(book_id):
    return render_template('showBook.html')


@app.route('/book/<int:book_id>/edit')
def editBook(book_id):
    return render_template('editBook.html')


@app.route('/book/<int:book_id>/delete')
def deleteBook(book_id):
    return render_template('deleteBook.html')


if __name__ == '__main__':
    app.debug = True
    app.secret_key = config.secret_key
    app.run(config.host, config.port)

