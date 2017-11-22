def print_args(*args, **kwargs):
    '''Metoda przyjmuje nieskonczona liczbe parametrow'''
    # typy argumentow
    print(type(args), type(kwargs))

    # argumenty pozycyjne
    for arg in args:
        print(arg)

    # argumenty nazwane
    for kw, kwarg in kwargs.items():
        print('{}={}'.format(kw, kwarg))


def args_to_list(*args):
    '''Metoda przyjmuje nieskonczona liczbe parametrow pozycyjnych'''
    return list(args)


def args_to_dict(**kwargs):
    '''Metoda przyjmuje nieskonczona liczbe parametrow nazwanych'''
    return dict(kwargs)


print_args('a', 'b', 'c', first=1, second=2, third=3)
print('args_to_list:', args_to_list('a', 'b', 'c'))
print('args_to_dict:', args_to_dict(first=1, second=2, third=3))
