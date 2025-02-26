from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


def get_mongodb():

    uri = "mongodb+srv://user16:567321@klimenko0212.6py6t.mongodb.net/?retryWrites=true&w=majority&appName=klimenko0212"
    # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client.hw_10

    return db