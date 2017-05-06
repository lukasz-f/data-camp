# Program z zajęć
import re, codecs
kolory = ['blue','red','yellow','black','gray','green']
with codecs.open('pg50133.txt', 'r', 'utf8') as dr:
    caly_tekst = dr.read()
    pattern = '|'.join(kolory)
    slowa_na_a = re.findall(r'\s+('+pattern+')\s+(\w+)', caly_tekst, re.UNICODE)
print(slowa_na_a)
