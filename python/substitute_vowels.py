def substitute_vowels(lst):
    '''Zastepuja samogloski znakami "*"'''

    replaced = []
    vowels = ['a', 'ą', 'e', 'ę', 'i', 'o', 'ó', 'u', 'y']
    for word in lst:
        for vowel in vowels:
            word = word.replace(vowel, '*')
        replaced.append(word)
    return replaced


def substitute_vowels2(lst):
    '''Zastepuja samogloski znakami "*"'''

    dest = []
    vowels = 'aeiouyąę'
    vowels += vowels.upper()
    for word in lst:
        for vowel in vowels:
            word = word.replace(vowel, '*')
        dest.append(word)
    return dest

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

print(substitute_vowels(words))
print(substitute_vowels2(words))
