def factory(n):
    '''Liczy silnie'''

    if n == 0:
        return 1
    else:
        return n * factory(n-1)


print('3! =', factory(4))
