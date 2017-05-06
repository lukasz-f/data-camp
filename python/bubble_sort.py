def bubble_sort(lst):
    '''Sortowanie bąbelkowe'''

    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]


def bubble_sort2(lst):
    '''Sortowanie bąbelkowe'''

    done = False
    while not done:
        done = True
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                done = False


l = [7, 3, 5, 2, 1, 100, 315, 3, 552, 61, 8, 2, 1, 10]
bubble_sort2(l)
print('Sorted list:', l)
