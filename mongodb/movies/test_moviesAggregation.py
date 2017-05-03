from unittest import TestCase
from MoviesAggregation import *
from pprint import pprint

class TestMoviesAggregation(TestCase):
    def setUp(self):
        self.movies = MoviesAggregation()

    def test_avg_revenue_from_movies(self):
        avg_rev = list(self.movies.avg_revenue_from_movies());
        pprint(avg_rev)
        self.assertEqual(len(avg_rev), 1)

    def test_avg_revenue_per_genre(self):
        avg_rev = list(self.movies.avg_revenue_per_genre());
        pprint(avg_rev)
        self.assertEqual(len(avg_rev), 41)

    def test_avg_revenue_by_george_lucas(self):
        avg_rev = list(self.movies.avg_revenue_by_george_lucas());
        pprint(avg_rev)
        self.assertEqual(len(avg_rev), 3)

    def test_starred_movies_per_actor(self):
        movies_count = list(self.movies.starred_movies_per_actor());
        pprint(movies_count)
        self.assertEqual(len(movies_count), 350)

    def test_top_3_most_profitable_directors(self):
        director_profit = list(self.movies.top_3_most_revenue_directors());
        pprint(director_profit)
        self.assertEqual(len(director_profit), 3)

    def test_top_5_most_profitable_movies(self):
        movies_profit = list(self.movies.top_5_most_profitable_movies());
        pprint(movies_profit)
        self.assertEqual(len(movies_profit), 5)
