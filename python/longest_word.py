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


def longest_word(lst):
    longest = ''
    for word in lst:
        if len(word) > len(longest):
            longest = word
    return longest


print('Longest word is: {}'.format(longest_word(words)))


def starts_with_capital(lst):
    dest = []
    for word in lst:
        if word[0].isupper():
            dest.append(word)
    return dest


print('Capitalized words: {}'.format(starts_with_capital(words)))


def substitute_vowels(lst):
    vowels = 'aeiouyęą'
    vowels += vowels.upper()
    dest = []
    for word in lst:
        for v in vowels:
            word = word.replace(v, '*')
        dest.append(word)
    return dest


print('Substituted vowels: {}'.format(substitute_vowels(words)))
