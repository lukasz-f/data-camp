from pymongo import MongoClient
from pprint import pprint

class MoviesAggregation:
    def __init__(self):
        db_name = 'pySamples'
        collection_name = 'movies'
        client = MongoClient('localhost', 27017)
        db = client[db_name]
        collection = db[collection_name]
        self.moviesCollection = collection

    # Średni przychód ze wszystkich filmów
    def avg_revenue_from_movies(self):
        pipeline = [
            { '$group':{
                "_id" : 'null',
                'avg_revenue' : {'$avg' : "$gross_revenue.amount"}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #1. Średni przychód z filmów per gatunek
    def avg_revenue_per_genre(self):
        pipeline = [
            {'$unwind': '$genre'},
            {'$group': {
                '_id': '$genre',
                 'avg_rev': {'$avg': '$gross_revenue.amount'}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #2. Suma przychodu z filmów wyreżyserowanych przez George Lucasa
    def avg_revenue_by_george_lucas(self):
        pipeline = [
            {'$match': {'directed_by': 'George Lucas'}},
            {'$group': {
                '_id': 'null',
                'sum_revenue': {'$sum': '$gross_revenue.amount'}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline, useCursor=False)
        return result

    #3. Ile razy akorzy występowali w filmach
    def starred_movies_per_actor(self):
        pipeline = None
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #4. TOP 3 przeciętnie najbardziej dochodowi dyrektorzy (średni przychód z filmów) - zwrócone nazwisko reżysera + średni przychód
    def top_3_most_revenue_directors(self):
        pipeline = None
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #5. TOP 5 filmów, które osigąnęły najwięszyk zysk (estimated_budget - gross_revenue)
    def top_5_most_profitable_movies(self):
        pipeline = None
        result = self.moviesCollection.aggregate(pipeline)
        return result

moviesAggregation = MoviesAggregation()
pprint(list(moviesAggregation.avg_revenue_from_movies()))
pprint(list(moviesAggregation.avg_revenue_per_genre()))
pprint(list(moviesAggregation.avg_revenue_by_george_lucas()))
