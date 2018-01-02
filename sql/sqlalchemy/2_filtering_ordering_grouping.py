# Import necessary module
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import and_
from sqlalchemy import desc
from sqlalchemy import func

# Create an engine to the census database
engine = create_engine('sqlite:///census.sqlite')
con = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table
stmt = select([census])

# Filter data selected from a Table - Simple
# Add a where clause to filter the results to only those for New York
stmt = stmt.where(census.columns.state == 'New York')

# Print the emitted statement to see the SQL emitted
print(stmt)

# Execute the statement
results = con.execute(stmt).fetchall()

# Loop over the results and print the age, sex, and pop2008
for result in results:
    print(result.age, result.sex, result.pop2008)


# Filter data selected from a Table - Expressions #
states = ['New York', 'California', 'Texas']

# Create a query for the census table where clause to match all the states in_ the list states
stmt = select([census]).where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in con.execute(stmt):
    print(result.state, result.pop2000)


# Filter data selected from a Table - Advanced #
# Build a query for the census table where clause to select only non-male records from California using and_
stmt = select([census]).where(
    # The state of California with a non-male sex
    and_(census.columns.state == 'California',
         census.columns.sex != 'M')
)

# Loop over the ResultProxy printing the age and sex
for result in con.execute(stmt):
    print(result.age, result.sex)


# Ordering by a Single Column #
# Build a query to select the state column
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results
results = con.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])


# Ordering in Descending Order by a Single Column #
# Build a query to select the state column
stmt = select([census.columns.state])

# Order stmt by state in descending order
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results
rev_results = con.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])


# Ordering by Multiple Columns #
# Build a query to select state and age
stmt = select([census.columns.state, census.columns.age])

# Append order by to ascend by state and descend by age
stmt = stmt.order_by(census.columns.state, desc(census.columns.age))

# Execute the statement and store all the records
results = con.execute(stmt).fetchall()

# Print the first 20 results
print(results[:20])


# Counting Distinct Data #
# Build a query to count the distinct states values
stmt = select([func.count(census.columns.state.distinct())])

# Execute the query and store the scalar result
distinct_state_count = con.execute(stmt).scalar()

# Print the distinct_state_count
print(distinct_state_count)


# Count of Records by State #
# Build a query to select the state and count of ages by state
stmt = select([census.columns.state, func.count(census.columns.age)])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records
results = con.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())


# Determining the Population Sum by State #
# Build an expression to calculate the sum of pop2008 labeled as population
pop2008_sum = func.sum(census.columns.pop2008).label('population')

# Build a query to select the state and sum of pop2008
stmt = select([census.columns.state, pop2008_sum])

# Group stmt by state
stmt = stmt.group_by(census.columns.state)

# Execute the statement and store all the records
results = con.execute(stmt).fetchall()

# Print results
print(results)

# Print the keys/column names of the results returned
print(results[0].keys())
