# Fibonacci rekurencja
def f(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x-1) + f(x-2)

# Fibonacci iteracja
def ff(x):
    a = 0
    b = 1
    c = 1
    for i in range(x):
        a = b
        b = c
        c = a + b
    return a

# Fibonacci iteracja 2
def fff(x):
    a, b = 0, 1
    for i in range(x):
        a, b = b, a + b
    return a
