from flask import Flask
import config


app = Flask(__name__)


# HOME ROUTE
@app.route('/')
@app.route('/books')
def showBooks():
    return 'route: / and /books ---- parameters: none'


# CATEGORY ROUTES
@app.route('/book/category/add')
def addBookCategory():
    return 'route: /book/category/add ---- parameters: none'


@app.route('/book/category/<int:book_cat_id>')
def showBookCategory(book_cat_id):
    return 'route: /book/category/<int:book_cat_add> ---- paramenters: {}'.format(book_cat_id)


@app.route('/book/category/<int:book_cat_id>/edit')
def editBookCategory(book_cat_id):
    return 'route: /book/category/<int:book_cat_add>/edit ---- paramenters: {}'.format(book_cat_id)


@app.route('/book/category/<int:book_cat_id>/delete')
def deleteBookCategory(book_cat_id):
    return 'route: /book/category/<int:book_cat_add>/delete ---- paramenters: {}'.format(book_cat_id)


# BOOK ROUTES
@app.route('/book/add')
def addBook():
    return 'route: /book/add ---- parameters: none'


@app.route('/book/<int:book_id>')
def showBook(book_id):
    return 'route: /book/<int:book_id> ---- parameters: {}'.format(book_id)


@app.route('/book/<int:book_id>/edit')
def editBook(book_id):
    return 'route: /book/<int:book_id>/edit ---- parameters: {}'.format(book_id)


@app.route('/book/<int:book_id>/delete')
def deleteBook(book_id):
    return 'route: /book/<int:book_id>/delete ---- parameters: {}'.format(book_id)


if __name__ == '__main__':
    app.debug = True
    app.run(config.host, config.port)

