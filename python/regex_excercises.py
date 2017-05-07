import re
import codecs

regex = r'([a-zA-Z]+) (\d+)'
strng = "June 24, August 9, Dec 12"
print(re.sub(regex, r'\2 of \1', strng))

print(re.findall(regex, strng))

matchlist = re.finditer(regex, strng)
for m in matchlist:
    print(m.group(1), m.group(2))

# Operacje należy przeprowadzić na pliku shakespeare.txt
# 1. Wybrać wszystkie słowa rozpoczynające się wielką literą.
with codecs.open('shakespeare.txt', 'r', 'utf8') as file:
    data = file.read()
    matchList = re.findall(r'\b[A-Z]\w+', data)
    #print(matchList)

# 2. Wybrać słowa kończące zdanie. Za słowo kończące zdanie uznajemy taki po którym
# następuje znak ., ? lub !
    matchList = re.findall(r'\w+[.,?!]', data)
    #print(matchList)

# 3. Wybrać każde słowo występujące po słowie 'The'.
    matchList = re.findall(r'The\s(\w+)', data)
    print(matchList)

# 4. Wybrać każde słowo występujące po słowie 'The' jeśli rozpoczyna się wielką literą.
"""5. Wybrać wszystkie liczby całkowite z tekstu
6. Wybrać słowo występujące przed i za słowem and.
7. Zamienić zdanie każde słowo w zdaniu na pisane wielkimi literami jeśli na końcu zdania jest wykrzyknik.
-------
Operacje należy przeprowadzić na pliku access_log.txt
1. Wybrać wszystkie adresy IP znajdujące się w logu.
2. Wybrać adresy których ostatni człon domeny to waw.pl
-------"""
