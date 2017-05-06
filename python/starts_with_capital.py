import re


def starts_with_capital(lst):
    '''Zwraca slowa zaczynajace sie duza litera'''

    capitals = []
    for word in lst:
        match = re.search(r'^[A-Z]', word)
        if match:
            capitals.append(word)
    return capitals


def starts_with_capital2(lst):
    '''Zwraca slowa zaczynajace sie duza litera'''

    capitals = []
    for word in lst:
        if word[0].isupper():
            capitals.append(word)
    return capitals

words = ['Początek', 'traktatu', 'czasu', 'być', 'wstrzemięźliwym', 'Tak',
             'może', 'być', 'uważana', 'jako', 'najwyższy', 'stopień', 'moralności',
             'z', 'części', 'Ale', 'się', 'od', 'Stworzyciela', 'niebył',
             'nadany', 'Jakże', 'to', 'mogło', 'być', 'moralna', 'a', 'jednak',
             'złą', 'sprawę', 'będzie', 'znowu', 'się', 'uczynkiem', 'ale', 'każdy',
             'będzie', 'znowu', 'się', 'łaskawego', 'przyjęcia', 'żegnam', 'się',
             'on', 'nieraz', 'zgryzot', 'sumienia', 'które', 'przybieramy', 'z',
             'czystego', 'serca', 'lub', 'obowiąski', 'które', 'człowiek', 'jako',
             'najwyższy', 'stopień', 'przyjaźni', 'świadczyć', 'lecz', 'tylko',
             'robakiem', 'tedy', 'jej', 'człowiek', 'w', 'Królewcu', 'szanowny',
             'Imanuel', 'Kant', 'Professor', 'filozofii', 'który', 'się', 'musiał',
             'od', 'Stworzyciela', 'niebył', 'nadany']

print(starts_with_capital(words))
print(starts_with_capital2(words))
