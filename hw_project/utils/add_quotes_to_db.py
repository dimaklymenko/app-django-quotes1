# import json
# from bson.objectid import ObjectId
#
# from pymongo import MongoClient
#
# client = MongoClient ("mongodb: //Localhost" )
#
# db = client.hw
#
# with open ('quotes_4.json', 'r', encoding='utf-8') as fd:
#     quotes = json.load(fd)
#
# for quote in quotes:
#     author = db.authors.find_one({'fullname': quote['author']})
#     if author:
#         db.quotes.insert_one({
#             'quote': quote['quote'],
#             'tags': quote['tags'],
#             'author': ObjectId(author['_id'])
#             })


# import json
# from bson.objectid import ObjectId
# from mongoengine import connect
#
#
# db = connect(
#     db= "hw_10" ,  # Назва вашої бази даних
#     username= "user16" ,  # Ім'я користувача
#     password="567321",  # Пароль
#     host="mongodb+srv://user16:567321@klimenko0212.6py6t.mongodb.net/?retryWrites=true&w=majority&appName=klimenko0212",  # Ваш MongoDB URI
# )
#
# with open ('quotes_4.json', 'r', encoding='utf-8') as fd:
#     quotes = json.load(fd)
#
# for quote in quotes:
#     author = db.authors.find_one({'fullname': quote['author']})
#     if author:
#         db.quotes.insert_one({
#             'quote': quote['quote'],
#             'tags': quote['tags'],
#             'author': ObjectId(author['_id'])
#             })


import json
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://user16:567321@klimenko0212.6py6t.mongodb.net/?retryWrites=true&w=majority&appName=klimenko0212"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.hw_10

with open ('quotes_4.json', 'r', encoding='utf-8') as fd:
    quotes = json.load(fd)

for quote in quotes:
    author = db.authors.find_one({'fullname': quote['author']})
    if author:
        db.quotes.insert_one({
            'quote': quote['quote'],
            'tags': quote['tags'],
            'author': ObjectId(author['_id'])
            })