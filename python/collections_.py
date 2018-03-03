from collections import Counter
from collections import defaultdict
from collections import OrderedDict

stations = ['Division/Milwaukee', 'Division/Milwaukee', 'Grand/State', 'Grand/State', 'Grand/State',
            'Kedzie-Homan-Forest Park', 'State/Lake', 'State/Lake',  'Cumberland', '79th']

# Create a Counter of the stations list
station_count = Counter(stations)

# Print the station_count
print(station_count)

# Find the 3 most common elements
print(station_count.most_common(3))


# Safely appending to a key's value int
# Create a defaultdict with a default type of int
station_amount = defaultdict(int)

# Count stations
for station in stations:
    station_amount[station] += 1

# Print the station_amount
print(station_amount)


# Working with OrderedDictionaries
# Create an OrderedDict
station_ordered = OrderedDict()

# Count stations
for station in stations:
    if station not in station_ordered:
        station_ordered[station] = 0
    station_ordered[station] += 1

# Print the first 31 records
print(list(station_ordered.items())[:3])

# Print the first key in ridership_date
print(list(station_ordered.keys())[0])

# Pop the first item from ridership_date and print it
print(station_ordered.popitem(last=False))

# Print the last key in ridership_date
print(list(station_ordered.keys())[-1])

# Pop the last item from ridership_date and print it
print(station_ordered.popitem())
