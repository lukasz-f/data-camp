# Create a 5 x 5 matrix using a list of lists
matrix = [[col for col in range(5)] for row in range(5)]

# Print the matrix
print(matrix)

# Create a num pairs
nums = [(num1, num2) for num1 in range(5) for num2 in range(5)]
print(nums)


# Create a list of strings
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension
new_fellowship = [member for member in fellowship if len(member) >=7]

# Print the new list
print(new_fellowship)


# Create list comprehension
new_fellowship = [member if len(member) >=7 else '' for member in fellowship]

# Print the new list
print(new_fellowship)

# See also: dict comprehensions, generators
