# Create a list of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension
new_fellowship = {member: len(member) for member in fellowship}

# Print the new list
print(new_fellowship)

# See also: list comprehensions, generators
