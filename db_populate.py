import db_controller

users = [
    {
        'name': 'admin',
        'email': 'admin@example.com',
        'picture': 'https://ichef.bbci.co.uk/news/660/cpsprodpb/025B/production/_85730600_monkey2.jpg',
        'role': 'admin'
    },
    {
        'name': 'johndoe',
        'email': 'john.doe@example.com',
        'picture': 'https://s-media-cache-ak0.pinimg.com/236x/01/59/40/01594057534c60f94af3165f26d85629.jpg',
        'role': 'user'
    },
    {
        'name': 'janedoe',
        'email': 'jane.doe@example.com',
        'picture': 'http://www.madadventurers.com/wp-content/uploads/2014/06/educated-monkey.jpg',
        'role': 'user'
    },
    {
        'name': 'bobsmith',
        'email': 'bob.smith@example.com',
        'picture': 'http://2.bp.blogspot.com/_JP9OiUP__qY/TOvdF0vZpaI/AAAAAAAAAlA/5EEo_gIifD0/s1600/funny-monkey-2.jpg',
        'role': 'user'
    },
    {
        'name': 'sallyspringer',
        'email': 'sally.springer@example.com',
        'picture': 'https://yt3.ggpht.com/-_IXzYFNWU8U/AAAAAAAAAAI/AAAAAAAAAAA/6tXWVmD0E64/s900-c-k-no-mo-rj-c0xffffff/photo.jpg',
        'role': 'user'
    },

]


categories = [
    {'name': 'Cookbooks'},
    {'name': 'Business'},
    {'name': 'Programming'},
    {'name': 'Health & Fitness'},
    {'name': 'Real Estate'}
]

# Keep in mind that a category_id and user_id must already exist. They will be
# created above and numbered sequentially.

books = [
    {
        'name': 'How To Bake Everything',
        'author': 'William Kent Krueger',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$32.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51beEtGlbTL._SX140_.jpg",
        'category_id': 1,
        'user_id': 1
    },
        {
        'name': 'Skinny Taste',
        'author': 'Mark Brittman',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$32.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51qNsBerPnL._SY160_.jpg",
        'category_id': 1,
        'user_id': 2
    },
        {
        'name': 'Everyday Cooking',
        'author': 'Alton Brown',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$20.34',
        'image': "https://images-na.ssl-images-amazon.com/images/I/618HY4mMq7L._SL140_.jpg",
        'category_id': 1,
        'user_id': 3
    },
        {
        'name': 'Better Baking',
        'author': 'Genevieve Ko',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$20.50',
        'image': "https://images-na.ssl-images-amazon.com/images/I/61dDjkvVAcL._SY160_.jpg",
        'category_id': 1,
        'user_id': 4
    },
        {
        'name': 'Cravings',
        'author': 'Chrissy Teigen',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$17.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51HGuoYiOZL._SY160_.jpg",
        'category_id': 1,
        'user_id': 5
    },
        {
        'name': 'Pitch Anything',
        'author': 'Oren Klaff',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$12.49',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51uL3d9q8CL._SY160_.jpg",
        'category_id': 2,
        'user_id': 1
    },
        {
        'name': 'Crucial Accountability',
        'author': 'Joseph Grenny',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$10.56',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51fm83XKmIL._SY160_.jpg",
        'category_id': 2,
        'user_id': 2
    },
        {
        'name': 'Security Analysis',
        'author': 'Benjamin Graham',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$49.75',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51JGSgsa6kL._SY160_.jpg",
        'category_id': 2,
        'user_id': 3
    },
        {
        'name': 'Influencer',
        'author': 'Kerry Patterson',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$10.56',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51ZFQv994YL._SY160_.jpg",
        'category_id': 2,
        'user_id': 4
    },
        {
        'name': 'Crucial Conversations',
        'author': 'Kerry Patterson',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$11.30',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51W9DU9pFuL._SY160_.jpg",
        'category_id': 2,
        'user_id': 5
    },
        {
        'name': 'JavaScript Patterns',
        'author': 'Stoyan Stefanov',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$19.07',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51%2BSiphz7AL._SY160_.jpg",
        'category_id': 3,
        'user_id': 1
    },
        {
        'name': 'CSS',
        'author': 'Eric A. Meyer',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$32.38',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51MfHgeKjAL._SY160_.jpg",
        'category_id': 3,
        'user_id': 2
    },
        {
        'name': 'HTML5',
        'author': 'Matthew MacDonald',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$29.29',
        'image': "https://images-na.ssl-images-amazon.com/images/I/41O0giH3mcL._SY160_.jpg",
        'category_id': 3,
        'user_id': 3
    },
        {
        'name': 'JavaScript & JQuery',
        'author': 'Jon Duckett',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$30.57',
        'image': "https://images-na.ssl-images-amazon.com/images/I/41oa41LdNdL._SY160_.jpg",
        'category_id': 3,
        'user_id': 4
    },
        {
        'name': 'Modern PHP',
        'author': 'Josh Lockhart',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$25.44',
        'image': "https://images-na.ssl-images-amazon.com/images/I/516kv5hpwuL._SY160_.jpg",
        'category_id': 3,
        'user_id': 5
    },
        {
        'name': 'The Big Book of Juices',
        'author': 'Natalie Savona',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$14.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51NTOxOlL4L._SY160_.jpg",
        'category_id': 4,
        'user_id': 1
    },
        {
        'name': 'Full Catastrophe Living',
        'author': 'Jon Kabat-Zinn',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$12.19',
        'image': "https://images-na.ssl-images-amazon.com/images/I/41-gkNC8JTL._SY160_.jpg",
        'category_id': 4,
        'user_id': 2
    },
        {
        'name': 'The Art of Learning',
        'author': 'Josh Waitzkin',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$11.22',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51p7Riv4tjL._SY160_.jpg",
        'category_id': 4,
        'user_id': 3
    },
        {
        'name': 'Fast After 50',
        'author': 'Joe Friel',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$15.79',
        'image': "https://images-na.ssl-images-amazon.com/images/I/61aLIJBq4pL._SY160_.jpg",
        'category_id': 4,
        'user_id': 4
    },
        {
        'name': 'Healing With Whole Foods',
        'author': 'Paul Pitchford',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$19.95',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51i3nucsfPL._SY160_.jpg",
        'category_id': 4,
        'user_id': 5
    },
        {
        'name': 'The Millionaire Real Estate Investor',
        'author': 'Gary Keller',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$12.86',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51E7ZEh-4bL._AC_US160_.jpg",
        'category_id': 5,
        'user_id': 1
    },
        {
        'name': 'Real Estate Investing for Dummies',
        'author': 'Eric Tyson',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$11.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/516F-238AiL._AC_US160_.jpg",
        'category_id': 5,
        'user_id': 2
    },
        {
        'name': 'How to Flip a House',
        'author': 'William Johnson',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$0.00',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51mCu8LOxuL._AC_US160_.jpg",
        'category_id': 5,
        'user_id': 3
    },
        {
        'name': 'Real Estate Investing',
        'author': 'Michael McCord',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$13.38',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51gamZ9mwLL._AC_US160_.jpg",
        'category_id': 5,
        'user_id': 4
    },
        {
        'name': 'Invest Without Banks',
        'author': 'Marki Rubel',
        'description': "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.",
        'price': '$1.99',
        'image': "https://images-na.ssl-images-amazon.com/images/I/51TgRJC5NhL._AC_US160_.jpg",
        'category_id': 5,
        'user_id': 5
    },
]


if __name__ == '__main__':
    db_controller.create_users(users)
    db_controller.create_categories(categories)
    db_controller.create_books(books)