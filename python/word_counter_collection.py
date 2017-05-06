'''
zadanie_python_01.txt
1. Statystyki wyrazów
- Należy napisać funkcję, który stworzy statystyki wyrazów z pliku text_sample.txt
Funkcja powinna zwracać słownik postaci
{'słowo': 1,
 'słowo2': 2}
 gdzie kluczami są słowa z pliku, a wartościami ilości ich wystąpień.
 Funkcja powinna zliczać słowa niezależnie od wielkości liter ('słowo' jest tym samym co 'SłOwo').

Należy w miarę możliwości użyć klas z modułu collections
- Dopisać funkcję sortującą wcześniej zebrane statystyki rosnąco wg. ilości wystąpień słowa.
- Dopisać funkcję wybierającą najdłuższe i najdłuższe słowo ze słownika statystyk
'''

import string
import codecs
from collections import Counter
from collections import OrderedDict


def file_stats():
    c = Counter()

    with codecs.open('text_sample.txt', 'r', 'utf8') as file:
        for each_line in file:
            for each_word in each_line.split():
                word = each_word.strip(string.punctuation).lower()
                c[word] += 1

    return dict(c)


def ordered_stats():
    stats = file_stats()
    new_stats = OrderedDict(sorted(stats.items(), key=lambda t: t[1]))
    return new_stats


def min_max_stats():
    stats = ordered_stats()
    items = list(stats.items())
    return items[0], items[-1]


print('--------Stats--------')
print(file_stats())
print('--------Ordered Stats--------')
print(ordered_stats())
print('--------Min Max--------')
print(min_max_stats())
