from unittest import TestCase
from MoviesQueries import *
from pprint import pprint



class TestMoviesQueries(TestCase):
    def setUp(self):
        self.movies = MoviesQueries()

    def test_count_movies(self):
        print('count_movies result:' + str(self.movies.count_movies()))
        self.assertEqual(self.movies.count_movies(), 51)

    def test_emma_watson_movies(self):
        emma_watson_movies = self.movies.emma_watson_movies();
        print('emma_watson_movies result:')
        pprint(list(emma_watson_movies))
        self.assertEqual(emma_watson_movies.count(), 8)

    def test_comedy_and_fantasy_movies(self):
        comedy_and_fantasy_movies = self.movies.comedy_and_fantasy_movies();
        print('comedy_and_fantasy_movies:')
        pprint(list(comedy_and_fantasy_movies))
        self.assertEqual(comedy_and_fantasy_movies.count(), 4)
