female_baby_names_2012 = {('ASHLEY', 64), ('ELEANOR', 48), ('MELANIE', 83), ('LONDON', 52), ('TALIA', 46)}
names = {}

# Loop over the dictionary tuples
for name, rank in female_baby_names_2012:
    names[rank] = name

# Loop over the keys of dictionary
for rank in names:
    print(rank)

# Print list of keys
print(names.keys())

# Nested dictionaries
boy_names = {2018: {1: 'Joseph', 2: 'David', 3: 'Michael'},
             2017: {1: 'David', 2: 'Joseph', 3: 'Michael'}}
print(boy_names[2018][1])
print(boy_names.get(2018).get(1))
print(boy_names.get(2018).get(4, 'Not Available'))

# Adding and extending dictionaries
boy_names[2016] = {1: 'Michael', 2: 'Joseph', 3: 'David'}
boy_names[2016].update([(1, 'Casey'), (2, 'Aiden')])
print(boy_names)

# Popping and deleting
print(boy_names.pop(2016))
print(boy_names.pop(2015, {}))
try:
    del(boy_names[2015])
except:
    pass

# Loop over the dictionary items
for name, rank in names.items():
    print(name, rank)
