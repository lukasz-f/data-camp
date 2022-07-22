import pymongo
import datetime
import pprint
import bson.objectid
from collections import OrderedDict

# Making a Connection
client = pymongo.MongoClient()
# client = pymongo.MongoClient('localhost', 27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# Get a list of names of the databases managed by client
client.list_database_names()

# Getting a Database
db = client.test_database
# db = client['test-database']

# Get a list of names of the collections managed by the test database
client.test_database.list_collection_names()

# Getting a Collection
collection = db.test_collection
# collection = db['test-collection']

# List all Collections in db
db.collection_names(include_system_collections=False)

# Documents
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow(),
        "prizes": []}
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
              "text": "First post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 10, 21, 14),
              "prizes": [
                  {"category": "physics",
                   "share": "4"},
                  {"category": "chemistry",
                   "share": "4"}
              ]},
             {"author": "Mike",
              "text": "Another post!",
              "tags": ["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14),
              "prizes": [
                  {"category": "chemistry",
                   "share": "1"}
              ]},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too!",
              "tags": ["mongodb"],
              "date": datetime.datetime(2009, 11, 10, 10, 45),
              "prizes": [] }]
result = posts.insert_many(new_posts)
result.inserted_ids

new_authors = [{"firstname": "Mike",
                "surname": "Antoon",
                "gender": "male"},
               {"firstname": "Eliot",
                "surname": "Curie",
                "gender": "female"}]
authors = db.authors
authors.insert_many(new_authors)

# Querying for More Than One Document
for post in posts.find():
    pprint.pprint(post)

for post in posts.find({"author": "Mike"}):
    pprint.pprint(post)

# Counting
posts.count_documents({})
posts.find({"author": "Mike"}).count()
posts.count_documents({"author": "Mike"})

# Filtering
posts.find({"author": "Mike", "text": "Another post!"})  # author == Mike and text == Another post!
posts.find({"$and": [{"author": "Mike"}, {"text": "Another post!"}]})  # author == Mike and text == Another post!
posts.find({"$or": [{"author": "Mike"}, {"text": "Another post!"}]})  # author == Mike or text == Another post!
posts.find({"$nor": [{"author": "Eliot"}, {"text": "Another post!"}]})  # author != Mike and text != Another post!
posts.find({"author": {"$not": {"$regex": "^M.*"}}})  # author != M*
posts.find({"text": {"$ne": "Another post!"} })  # text != Another post!
posts.find({"author": {"$in": ["Mike", "Eliot"]} })  # author == Mike or author == Eliot
posts.find({"author": {"$nin": ["Mike", "Eliot"]} })  # author != Mike and author != Eliot
posts.find({"tags": {"$exists": True} })  # tags field in document
posts.find({"tags.0": {"$exists": True} })  # tags != [] and tags != None
posts.find({"tags.2": {"$exists": True} })  # len(tags) >= 3
posts.find({"tags": "mongodb"})  # search "mongodb" value in array
posts.find({"tags": ["mongodb"]})  # search for ["mongodb"] array
posts.find({"prizes.category": "chemistry", "prizes.share": "1"})
posts.find({"prizes": {"$elemMatch": {"category": "chemistry", "share": "1"}}})

# Projection
posts.find(filter={}, projection={"author": 1, "_id": 0})  # return only author field
posts.find(projection={"prizes.category": 1, "_id": 0})  # return only category field of prizes array
posts.find({"prizes.category": {"$exists": True}}, ["prizes.category"])  # return prizes.category and _id when prizes.category exists

# Sorting
posts.find(sort=[("author", 1)])
posts.find(sort=[("author", 1), ("title", -1)])  # array of tupple because in Python < 3.7 dictionary's keys are not staying in order

# Limits
posts.find({}, limit=3)
posts.find({}, skip=3, limit=3)

# Method chaining
posts.find().sort().skip().limit()  # == posts.find().limit().skip().sort()

# Distinct
posts.distinct("author")  # ['Eliot', 'Mike']
posts.distinct('prizes.category')  # ['physics', 'chemistry']
posts.distinct('prizes.category', {'prizes.share': 4})  # ['physics']

# Range Queries
d = datetime.datetime(2009, 11, 12, 12)
for post in posts.find({"date": {"$lt": d}}).sort("author"):
    pprint.pprint(post)

# Indexing
posts.index_information()  # always index on _id field
posts.find().explain()  # query plan: COLSCAN - full collection scan, IXSCAN - index scan
# Create index
posts.create_index([('author', 1)])  # ascending index
posts.create_index([('author', 1), ('date', -1)])
# Create the unique index
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)], unique=True)
sorted(list(db.profiles.index_information()))

# Insert duplicate profile
user_profiles = [{'user_id': 211, 'name': 'Luke'},
                 {'user_id': 212, 'name': 'Ziltoid'}]
result = db.profiles.insert_many(user_profiles)
duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
result = db.profiles.insert_one(duplicate_profile)

# Aggregation
posts.aggregate([
    {"$match": {"author": "Mike"}},
    {"$project": {"text": 1, "_id": 0}},
    {"$sort": OrderedDict([("date", 1)])},
    {"$skip": 1},
    {"$limit": 3}
])  # posts.find(filter={"author": "Mike"}, projection={"text": 1, "_id": 0}, sort=[("date", 1)], skip=1, limit=3)

posts.aggregate([
    {"$match": {"author": "Mike"}},
    {"$count": "n_Mike_author"}
])  # posts.count_documents({"author": "Mike"})

# Field expressions with operators and field paths
# .aggregate([{ stage: { field: expression }}])
# .aggregate([{ stage: { field: { operator: [ parameters ] } }}])
posts.aggregate([
    {"$project": {"n_prizes": {"$size": ["$prizes"]}}}
])  # count prizes and return as n_prizes field

posts.aggregate([
    {"$project": {"n_prizes": {"$size": ["$prizes"]}}},
    {"$group": {"_id": None, "n_prizes_total": {"$sum": "$n_prizes"}}}
])  # count prizes in total

posts.aggregate([
    {"$project": {"solo_winner": {"$in": ["1", "$prizes.share"]}}}
])  # return True if array prizes share contains string value "1"

posts.aggregate([
    {"$addFields": {"solo_winner": {"$in": ["1", "$prizes.share"]}}}
])  # add new field with True if array prizes share contains string value "1"

posts.aggregate([
    {"$project": {"authorMike": {"$setEquals": [["$author"], ["Mike"]]}}}
])  # return True if author == Mike

posts.aggregate([
    {"$group": {"_id": "$author", "dates": {"$addToSet": "$date"}}}
])  # list all dates for each author

posts.aggregate([
    {"$unwind": "$tags"},
    {"$group": {"_id": "$author", "tags": {"$addToSet": "$tags"}}}
])  # list all tags for each author

posts.aggregate([
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "n_posts": {"$sum": 1}}}
])  # count posts for each tag

posts.aggregate([
    # get author from authors collection with left outer join
    {"$lookup": {"from": "authors", "foreignField": "firstname", "localField": "author", "as": "author_info"}},

    # unwind new author_info array
    {"$unwind": "$author_info"},

    # rename field author_info.surname to surname
    {"$project": {"author": 1, "author_info.gender": 1, "surname": "$author_info.surname"}},

    # group by fullname and collect genders
    {"$group": {"_id": {"$concat": ["$author", " ", "$surname"]},
                "genders": {"$addToSet": "$author_info.gender"}}}
])
