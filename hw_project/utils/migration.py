import os
import django
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hw_project.settings")
django.setup()

from quotes.models import Quote, Tag, Author # noqa

uri = "mongodb+srv://user16:567321@klimenko0212.6py6t.mongodb.net/?retryWrites=true&w=majority&appName=klimenko0212"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.hw_10

authors = db.authors.find()

for author in authors:
    Author.objects.get_or_create(
        fullname=author['fullname'],
        born_date=author['born_date'],
        born_location=author['born_location'],
        description=author['description']
    )

quotes = db.quotes.find()

for quote in quotes:
    tags = []
    for tag in quote['tags']:
        t, *_ = Tag.objects.get_or_create(name=tag)
        tags.append(t)

    exist_quote = bool(len(Quote.objects.filter(quote = quote['quote'])))

    if not exist_quote:
        author = db.authors.find_one({'_id': quote['author']})
        a = Author.objects.get(fullname=author['fullname'])
        q = Quote.objects.create(
            quote = quote['quote'],
            author = a
        )
        for tag in tags:
            q.tags.add(tag)