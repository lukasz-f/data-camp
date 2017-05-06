class MyList(list):
    def __eq__(self, other):
        return len(self ) == len(other)


l1 = MyList([1, 2, 3, 4])
l2 = MyList([11, 22, 33, 44])
print(l1 == l2)
