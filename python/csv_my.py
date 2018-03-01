# Import the python CSV module
import csv

# Create a python file object in read mode for the baby_names.csv file: csvfile
csvfile = open('../datasets/cars.csv', 'r')
cars = {}

# Loop over a csv reader on the file object
for row in csv.reader(csvfile):
    # Print each row
    print(row)
    # Add the country id and country name to the dictionary
    cars[row[0]] = row[2]

# Print the dictionary keys
print(cars.keys())
csvfile.close()


csvfile = open('../datasets/cars.csv', 'r')
cars = {}
for row in csv.DictReader(csvfile):
    print(row)
    cars[row['country_id']] = row['country']
print(cars.keys())
csvfile.close()
