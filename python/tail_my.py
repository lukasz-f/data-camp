'''
zadanie_python_01.txt
2. Stworzyć narzędzie działające jak systemowa komenda tail
Komenda powinna przyjmować jako argument plik, albo wejście z STDIN i wyświetlać na ekranie
ostatnie 5 linii danego pliku.

UWAGA: Do obsługi plików i wejścia STDIN można użyć modułu fileinput.

Należy w miarę możliwości użyć klas dostępnych w module collections.
'''

import fileinput
from collections import deque

q = deque(maxlen=5)

for line in fileinput.input():
    q.append(line)

for line in q:
    print(line, end='')
