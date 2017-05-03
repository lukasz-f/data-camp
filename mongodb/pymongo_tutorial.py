import pymongo
import datetime
import pprint
import bson.objectid

# Making a Connection
client = pymongo.MongoClient()
# client = pymongo.MongoClient('localhost', 27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# Getting a Database
db = client.test_database
# db = client['test-database']

# Getting a Collection
collection = db.test_collection
# collection = db['test-collection']

# List all Collections in db
db.collection_names(include_system_collections=False)

# Documents
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
pprint.pprint(post)
posts = db.posts

# Inserting a Single Document
result = posts.insert_one(post)
post_id = result.inserted_id

# Getting a Single Document
posts.find_one()
posts.find_one({"author": "Mike"})
posts.find_one({"_id": post_id})

# convert the ObjectId from a string
bson.objectid.ObjectId(str(post_id))

# Bulk Inserts
new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
result.inserted_ids

# Querying for More Than One Document
for post in posts.find():
    pprint.pprint(post)

for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)

# Counting
posts.count()
posts.find({"author": "Mike"}).count()

# Range Queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)

# Indexing
# Create the unique index
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))

# Insert duplicate profile
user_profiles = [{'user_id': 211, 'name': 'Luke'},
                 {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(duplicate_profile)
