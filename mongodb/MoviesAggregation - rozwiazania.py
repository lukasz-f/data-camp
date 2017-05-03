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
            {'$unwind': "$genre"},
            { '$group':{
                "_id" : '$genre',
                'avg_revenue' : {'$avg' : "$gross_revenue.amount"}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #2. Suma przychodu z filmów wyreżyserowanych przez George Lucasa
    def avg_revenue_by_george_lucas(self):
        pipeline = [
            {'$match': {"directed_by": "George Lucas"}},
            { '$group':{
                "_id" : '$genre',
                'sum_revenue' : {'$sum' : "$gross_revenue.amount"}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline, useCursor=False)
        return result

    #3. Ile razy akorzy występowali w filmach
    def starred_movies_per_actor(self):
        pipeline = [
            {'$unwind': "$starring"},
            { '$group':{
                "_id" : '$starring.actor',
                'moviesCount' : {'$sum' : 1}
                }
            }
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #4. TOP 3 przeciętnie najbardziej dochodowi dyrektorzy (średni przychód z filmów) - zwrócone nazwisko reżysera + średni przychód
    def top_3_most_revenue_directors(self):
        pipeline = [
        {'$project': {'gross_revenue': 1, 'directed_by': 1}},
        {'$unwind': "$directed_by"},
        {'$group': {'_id': "$directed_by",
                  'avg_income': {'$avg': "$gross_revenue.amount"}}},
        {'$sort': {'avg_income': -1}},
        {'$limit': 3}
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result

    #5. TOP 5 filmów, które osigąnęły najwięszyk zysk (estimated_budget - gross_revenue)
    def top_5_most_profitable_movies(self):
        pipeline = [
        {'$project': {'name': 1, "profit": {'$subtract': ["$gross_revenue.amount", "$estimated_budget.amount"]}}},
        {'$sort': {"profit": -1}},
        {'$limit': 5}
        ]
        result = self.moviesCollection.aggregate(pipeline)
        return result