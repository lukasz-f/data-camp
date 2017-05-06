def capitalize_consonants(sentence):
    '''Duze samogloski'''
    dest = []
    vowels = 'aeiouyąę'
    vowels += vowels.upper()
    for word in sentence.split():
        for letter in word:
            if letter not in vowels:
                word = word.replace(letter, letter.upper())
        dest.append(word)
    return ' '.join(dest)


print(capitalize_consonants('Ala ma kota'))
