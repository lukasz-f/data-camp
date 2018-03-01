mutants = ['charles xavier', 'bobby drake', 'kurt wagner', 'max eisenhardt', 'kitty pride']
aliases = ['prof x', 'iceman', 'nightcrawler', 'magneto', 'shadowcat']
powers = ['telepathy', 'thermokinesis', 'teleportation', 'magnetokinesis', 'intangibility']

# Create a list of tuples
mutant_data = list(zip(mutants, aliases, powers))

# Print the list of tuples
print(mutant_data)

# Re-create a zip object using the three lists
mutant_zip = zip(mutants, aliases, powers)

# Print the zip object
print(mutant_zip)

# Unpack the zip object and print the tuple values
for value1, value2, value3 in mutant_zip:
    print(value1, value2, value3)

# Unpacking with *
print(*zip(mutants, aliases, powers))

# Create dictionary from zip object
mutant_dict = dict(zip(aliases, powers))
print(mutant_dict)

# Zip & unzip
mutant_zip = zip(mutants, aliases, powers)
mutants_, aliases_, powers_ = zip(*mutant_zip)
print(mutants_, aliases_, powers_)
