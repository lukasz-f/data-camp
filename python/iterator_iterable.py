flash1 = ['jay garrick', 'barry allen', 'wally west', 'bart allen']
print('iterable:', type(flash1))

flash2 = iter(flash1)
print('iterator:', type(flash2))

# Print each item from the iterable
for person in flash1:
    print(person)

# Print each item from the iterator
print(next(flash2))
print(next(flash2))
print(next(flash2))
print(next(flash2))

# Print the sum of iterable 
print('Iterable len:', sum(list(range(3))))

# Get the sum of iterator
print('Iterator len:', sum(iter(range(3))))
      
# Iterating at once with *
print('Data:', *iter('Data'))
