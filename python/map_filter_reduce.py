# Import reduce from functools
from functools import reduce

# Create a list of strings
spells = ["protego", "accio", "expecto patronum", "legilimens"]

# Use map() to apply a lambda function over spells
shout_spells = map(lambda item: item + '!!!', spells)

# Convert shout_spells to a list
shout_spells_list = list(shout_spells)

# Convert shout_spells into a list and print it
print(shout_spells_list)


# Convert list of strings to floats with map
s_list = ['1', '2', '3']
f_map = map(float, s_list)
print(list(f_map))


# Create a list of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Use filter() to apply a lambda function over fellowship
result = filter(lambda member: len(member) > 6, fellowship)

# Convert result to a list
result_list = list(result)

# Convert result into a list and print it
print(result_list)


# Create a list of strings
stark = ['robb', 'sansa', 'arya', 'eddard', 'jon']

# Use reduce() to apply a lambda function over stark
result = reduce(lambda item1, item2: item1 + item2, stark)

# Print the result
print(result)
