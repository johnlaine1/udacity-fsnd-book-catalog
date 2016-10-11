from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from flask import session as login_session
import random, string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import db_controller
import config


app = Flask(__name__)


##### AUTHENTICATION #####
# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully logged out.")
        return redirect(url_for('showBooksFront'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showBooksFront'))
        

@app.route('/fbconnect', methods=['POST'])
def fbconnect():
  # Check state to prevent against cross site forgery attacks.
  if request.args.get('state') != login_session['state']:
    response = make_response(json.dumps('Invalid state parameter.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  access_token = request.data

  # Exchange client token for long-lived server-side token with 
  # GET /oauth/access_token?grant_type=fb_exchange_token&
  #   client_id={app-id}&client_secret={app-secret}&fb_exchange_token={short-lived-token}
  app_id = json.loads(open('oauth_credentials/client_secret_fb.json', 'r').read())['web']['app_id']
  app_secret = json.loads(open('oauth_credentials/client_secret_fb.json', 'r').read())['web']['app_secret']
  url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id={}&client_secret={}&fb_exchange_token={}'.format(app_id, app_secret, access_token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]

  # Use token to get user info from API
  userinfo_url = 'https://graph.facebook.com/v2.2/me'
  # Strip expire tag from access token
  token = result.split('&')[0]

  # Populate the login_session object
  url = 'https://graph.facebook.com/v2.4/me?{}&fields=name,id,email'.format(token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  data = json.loads(result)
  login_session['provider'] = 'facebook'
  login_session['username'] = data['name']
  login_session['email'] = data['email']
  login_session['facebook_id'] = data['id']

  # Get user picture - Facebook requires a separate call for this.
  url = 'https://graph.facebook.com/v2.2/me/picture?{}&redirect=0&height=200&width=200'.format(token)
  h = httplib2.Http()
  result = h.request(url, 'GET')[1]
  data = json.loads(result)
  login_session['picture'] = data['data']['url']

  # Check if user exists, if not create one.
  user_id = db_controller.get_user_id_from_email(login_session['email'])
  if not user_id:
    user_id = db_controller.create_user_from_session(login_session)
  login_session['user_id'] = user_id

  output = ''
  output += '<h1>Welcome, '
  output += login_session['username']
  output += '!</h1>'
  output += '<img src="'
  output += login_session['picture']
  output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
  flash("you are now logged in as %s" % login_session['username'])
  return output  
  

@app.route('/fbdisconnect')
def fbdisconnect():
  facebook_id = login_session['facebook_id']
  url = 'https://graph.facebook.com/{}/permissions'.format(facebook_id)
  h = httplib2.Http()
  h.request(url, 'DELETE')[1]


@app.route('/gconnect', methods=['POST'])
def gconnect():
    client_id = json.loads(
        open('oauth_credentials/client_secret_google.json', 'r').read())['web']['client_id']
        
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    print code
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('oauth_credentials/client_secret_google.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    
    if result['issued_to'] != client_id:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    
    # Store the access token in the session for later use.
    login_session['provider'] = 'google'
    login_session['credentials'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info and populate login_session
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # Check if user exists, if not create one.
    user_id = db_controller.get_user_id_from_email(login_session['email'])
    if not user_id:
      user_id = db_controller.create_user_from_session(login_session)
    login_session['user_id'] = user_id
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s" % login_session['username'])
    return output

# Disconnect - Revoke a current user's token and reset their login_session.
@app.route('/gdisconnect')
def gdisconnect():
  # Only disconnect a connected user.
  credentials = login_session.get('credentials')
  if credentials is None:
    response = make_response(json.dumps('Current user not connected.'), 401)
    response.headers['Content-Type'] = 'application/json'
    return response

  # Execute HHTP GET request to revoke current token.
  access_token = credentials
  url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
  h = httplib2.Http()
  result = h.request(url, 'GET')[0]

  if result['status'] == '200':
    response = make_response(json.dumps('Successfully disconnected.'), 200)
    response.headers['Content-Type'] = 'application/json'
    return response
  else:
    # If for some reason the token was invalid.
    response = make_response(json.dumps('Failed to revoke token for given user.', 400))
    response.headers['Content-Type'] = 'application/json'
    return response


# LOGIN
# Create anti-forgery state token
@app.route('/login')
def showLogin():
    categories = db_controller.get_categories()
    google_client_id = json.loads(
        open('oauth_credentials/client_secret_google.json', 'r').read())['web']['client_id']
    fb_app_id = json.loads(open('oauth_credentials/client_secret_fb.json', 'r').read())['web']['app_id']
    
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', categories = categories, STATE = state,
                            google_client_id = google_client_id, fb_app_id = fb_app_id)
    
    
##### HOME ROUTE #####
@app.route('/')
@app.route('/books')
def showBooksFront():
    categories = db_controller.get_categories()
    books = db_controller.get_recent_books(5)
    return render_template('front.html', categories = categories,
                            recent_books = books)


##### CATEGORY ROUTES #####

# ADD A CATEGORY
@app.route('/book/category/add', methods=['GET', 'POST'])
def addBookCategory():
    categories = db_controller.get_categories()
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
    
    if request.method == "GET":
        return render_template('addBookCategory.html', categories = categories)
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
                            categories = categories, 
                            current_category = current_category,
                            books = books)

# EDIT A CATEGORY
@app.route('/book/category/<int:book_cat_id>/edit', methods=['GET', 'POST'])
def editBookCategory(book_cat_id):
    categories = db_controller.get_categories()
    category = db_controller.get_category(book_cat_id)
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
        
    if request.method == 'GET':
        return render_template('editBookCategory.html', category = category,
                                categories = categories)
    if request.method == 'POST':
        category = db_controller.update_category(id = category.id, 
                                                 name = request.form['name'])
        return redirect(url_for('showBookCategory', book_cat_id = category.id))


# DELETE A CATEGORY
@app.route('/book/category/<int:book_cat_id>/delete', methods=['GET', 'POST'])
def deleteBookCategory(book_cat_id):
    categories = db_controller.get_categories()
    category = db_controller.get_category(book_cat_id)
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
        
    if request.method == "GET":
        return render_template('deleteBookCategory.html', category = category,
                                categories = categories)
    else:
        db_controller.delete_category(category.id)
        return redirect(url_for('showBooksFront'))


##### BOOK ROUTES #####

# ADD A BOOK
@app.route('/book/add', methods=['GET', 'POST'])
def addBook():
    categories = db_controller.get_categories()
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('You must first login before creating a new book')
        return redirect('/login')
        
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
    categories = db_controller.get_categories()
    book = db_controller.get_book(book_id)
    
    return render_template('showBook.html', book = book, categories = categories)

# EDIT A BOOK
@app.route('/book/<int:book_id>/edit', methods=['GET', 'POST'])
def editBook(book_id):
    categories = db_controller.get_categories()
    book = db_controller.get_book(book_id)
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
        
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
    categories = db_controller.get_categories()
    book = db_controller.get_book(book_id)
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
        
    if request.method == 'GET':
        return render_template('deleteBook.html', book = book, categories = categories)
    if request.method == 'POST':
        book = db_controller.delete_book(book.id)
        return redirect(url_for('showBooksFront'))

##### ADMIN ROUTES #####
@app.route('/admin')
def adminMain():
    users = db_controller.get_users()
    categories = db_controller.get_categories()
    books = db_controller.get_books()
    
    # Redirect to login if user is not logged in.
    if 'username' not in login_session:
        flash('Please login first')
        return redirect('/login')
        
    return render_template('admin.html', users = users, categories = categories, books = books)

if __name__ == '__main__':
    app.debug = True
    app.secret_key = config.secret_key
    app.run(config.host, config.port)

