import collections

# ChainMap (agreguje słowniki)
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'a': 5, 'f': 6}
cm = collections.ChainMap(d1, d2, d3)  # kolejnosc ma znaczenie przy zduplikowanych kluczach

# Zwraca pierwszy odnaleziony klucz
cm['a']  # 1
cm['a'] = 11  # zapisuje wartosc w chainmapie i oryginalnym słowniku
cm  # ChainMap({'a': 11, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
d1  # {'a': 11, 'b': 2}

cm.maps

# Tworzy nowa chainmape i dodaje na poczatek nowy slownik
cm.new_child({'g': 7, 'h': 8})

# Tworzy nowa chainmape ktora nie zawiera pierwszego slownika
cm.parents


# namedtuple krotka z nazwa
Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
p[0] + p[1]
p.x + p.y
x, y = p


# OrderedDict slownik z kolejnoscia elementów
od = collections.OrderedDict(d1)
od['x'] = 999
od.popitem()  # Pobiera i usuwa ze slownika ostatni element
od.popitem(last=False)  # Pobiera i usuwa ze slownik pierwszy element
od.move_to_end()  # Przesuwa element na koniec lub poczatek


# Counter
# Counter dla list zlicza ilosc wystapien danej wartosci
# Counter dla slownikow wartosc jest licznikiem dla klucza
c = collections.Counter([1, 2, 3, 1, 2, 1])
c.elements()  # iterator
c.most_common(5)  # Zwraca liste 5 najbardziej licznych elementow
c.fromkeys(iterable)


# deque (double ended queue) LIFO i FIFO
# Metody dostepu do elementow na koncach kontenera maja zlozonosc obliczeniowa O(1).
# W przypadku zwyklej listy zlozonosc obliczeniowa metod pop(0), insert(0, value) wynosi O(n).
# Przy tworzeniu obiektu mozna podac maksymalna wielkosc kontenera maxlen.
# jesli podano maxlen po osiagnieciu ostatniej pozycji kolejne elementy beda usuwane z drugiej strony kontenera
append()  # dodaje na koncu
appendleft()  # dodaje na poczatku
clear()  # usuwa wszystkie elementy
copy()  # Tworzy plytka kopie
count(x)  # Zwraca ilosc elementow rownych x
extend()  # Rozszerza o nowe elementy na koncu
extendleft()  # Rozszerza o nowe elementy na poczatku. Nowe elementy beda dodane w odwroconej kolejnosci
index()  # zwraca pozycje elementu x w kontenerze
insert(i, x)
pop()  # Zwraca ostatni element i usuwa go
popleft()  # Zwraca pierwszy element i usuwa go
remove(value)  # Usuwa pierwsze wystapienie elementu
reverse()  # Odwraca elementy listy
rotate(n)  # d.appendlift(d.pop())
maxlen  # Długosc kolekcji. Tylko do odczytu
