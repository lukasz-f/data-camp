def is_palindrom(word):
    '''Sprawdza czy słowo jest palindromem'''

    if len(word) == 0 or len(word) == 1:
        return True
    if word[0] == word[-1]:
        return is_palindrom(word[1:-1])
    else:
        return False

print('is palindrom:', is_palindrom('kajak'))
print('is palindrom:', is_palindrom('abba'))
