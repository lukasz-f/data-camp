def revert_sentence(sentence):
    '''Zdanie od tylu'''

    return ' '.join(reversed(sentence.split()))

print(revert_sentence('Ala ma kota'))
