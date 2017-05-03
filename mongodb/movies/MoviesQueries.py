from pymongo import MongoClient
from pprint import pprint

class MoviesQueries:
    def __init__(self):
        db_name = 'pySamples'
        collection_name = 'movies'
        client = MongoClient('localhost', 27017)
        db = client[db_name]
        collection = db[collection_name]
        self.moviesCollection = collection

    # 1. Uzupełnij metodę zwracająca ilośc wszystkich filmów
    def count_movies(self):
        count = self.moviesCollection.count()
        return count;
    # 2. Uzupełnij metodę zwracająca wszystkie filmy, w których wystąpiła Emma Watson
    def emma_watson_movies(self):
        ew_movies = self.moviesCollection.find({"starring.actor": "Emma Watson"})
        return ew_movies;

    # 3. Uzupełnij metodę zwracająca wszystkie filmy posiadające gatunek comedy oraz(and) fantasy
    def comedy_and_fantasy_movies(self):
        caf_movies = self.moviesCollection.find({'$and': [{'genre': 'Comedy'}, {'genre': 'Fantasy'}]}, {'name': 1, "_id": 0})
        return caf_movies

moviesQuery = MoviesQueries()
pprint(moviesQuery.count_movies())
#pprint(list(moviesQuery.emma_watson_movies()))
pprint(list(moviesQuery.comedy_and_fantasy_movies()))
