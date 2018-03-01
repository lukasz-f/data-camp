# Creating Sets
cookies_eaten_today = ['chocolate chip', 'peanut butter', 'chocolate chip', 'oatmeal cream', 'chocolate chip']
types_of_cookies_eaten = set(cookies_eaten_today)
print(types_of_cookies_eaten)


# Modifying Sets
# Add single element
types_of_cookies_eaten.add('biscotti')
types_of_cookies_eaten.add('chocolate chip')
print(types_of_cookies_eaten)

# Merge in another set or list
cookies_hugo_ate = ['chocolate chip', 'anzac']
types_of_cookies_eaten.update(cookies_hugo_ate)
print(types_of_cookies_eaten)


# Removing data
# Removes element by value
types_of_cookies_eaten.discard('biscotti')
print(types_of_cookies_eaten)

# Removes element
print(types_of_cookies_eaten.pop())
print(types_of_cookies_eaten.pop())


# Sets Similarities (or, and, -)
cookies_jason_eaten = set(['chocolate chip', 'oatmeal cream', 'peanut butter'])
cookies_hugo_ate = ['chocolate chip', 'anzac']
print(cookies_jason_eaten.union(cookies_hugo_ate))
print(cookies_jason_eaten.intersection(cookies_hugo_ate))
print(cookies_jason_eaten.difference(cookies_hugo_ate))
