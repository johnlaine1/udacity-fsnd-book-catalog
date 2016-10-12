import db_controller

users = [{'name': 'admin', 
        'email': 'admin@example.com', 
        'picture': 'https://ichef.bbci.co.uk/news/660/cpsprodpb/025B/production/_85730600_monkey2.jpg',
        'role': 'admin'},
        {'name': 'billmurray', 
        'email': 'bill.murray@example.com', 
        'picture': 'https://s-media-cache-ak0.pinimg.com/236x/01/59/40/01594057534c60f94af3165f26d85629.jpg',
        'role': 'user'}]
        

categories = [{'name': 'Fiction'},
              {'name': 'Romance'},
              {'name': 'Programming'},
              {'name': 'Real Estate'},
              {'name': 'Health & Fitness'}]
              
# Keep in mind that a category_id and user_id must already exist. They will be
# created above and numbered sequentially.

books = [{'name': 'Ordinary Grace',
          'author': 'William Kent Krueger',
          'description': "That was it. That was all of it. A grace so ordinary there was no reason at all to remember it. Yet I have never across the forty years since it was spoken forgotten a single word",
          'price': '$32.99',
          'image': "https://images-na.ssl-images-amazon.com/images/I/51qWp0x6aAL.jpg",
          'category_id': 1,
          'user_id': 1}]
          

if __name__ == '__main__':
    db_controller.create_users(users)
    db_controller.create_categories(categories)
    db_controller.create_books(books)