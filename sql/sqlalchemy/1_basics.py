# Import necessary module
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import select

# Create an engine to the census database
engine = create_engine('sqlite:///census.sqlite')

# Use the .table_names() method on the engine to print the table names
print(engine.table_names())


# Database metadata #
metadata = MetaData()
# Reflect census table from the engine
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print census table metadata
print(repr(census))

# Print the column names
print(census.columns.keys())

# Print census table metadata (another way)
print(repr(metadata.tables['census']))

# Print the column names (another way)
print(repr(metadata.tables['census'].columns.keys()))


# SQL Queries #
# Build select statement for census table
stmt = select([census])

# Print the emitted statement to see the SQL emitted
print(stmt)

# Open engine connection
con = engine.connect()

# Execute the statement
results = con.execute(stmt).fetchall()

# Print the results
print(results)


# Handling a ResultSet #
# Get the first row of the results by using an index
first_row = results[0]

# Print the first row of the results
print(first_row)

# Print the first column of the first row by using an index
print(first_row[0])

# Print the 'state' column of the first row by using its name
print(first_row['state'])
