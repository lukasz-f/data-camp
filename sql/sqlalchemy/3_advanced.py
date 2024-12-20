from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import select
from sqlalchemy import desc
from sqlalchemy import func
from sqlalchemy import case, cast, Float

engine = create_engine('sqlite:///census.sqlite')
con = engine.connect()
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Calculating a Difference between Two Columns #
# Build query to return state names by population difference from 2008 to 2000: stmt
stmt = select([census.columns.state, (census.columns.pop2008-census.columns.pop2000).label('pop_change')])

# Append group by for the state: stmt
stmt = stmt.group_by(census.columns.state)

# Append order by for pop_change descendingly: stmt
stmt = stmt.order_by(desc('pop_change'))

# Return only 5 results: stmt
stmt = stmt.limit(5)

# Use connection to execute the statement and fetch all results
results = con.execute(stmt).fetchall()

# Print the state and population change for each record
for result in results:
    print('{}:{}'.format(result.state, result.pop_change))


# case, cast, Float #
# Build an expression to calculate female population in 2000
female_pop2000 = func.sum(
    case([
        (census.columns.sex == 'F', census.columns.pop2000)
    ], else_=0))

# Cast an expression to calculate total population in 2000 to Float
total_pop2000 = cast(func.sum(census.columns.pop2000), Float)

# Build a query to calculate the percentage of females in 2000
stmt = select([female_pop2000 / total_pop2000* 100])

# Execute the query and store the scalar result
percent_female = con.execute(stmt).scalar()

# Print the percentage
print(percent_female)


# Automatic Joins with an Established Relationship #
# Build a statement to join census and state_fact tables
state_fact = Table('state_fact', metadata, autoload=True, autoload_with=engine)
stmt = select([census.columns.pop2000, state_fact.columns.abbreviation])

# Execute the statement and get the first result
result = con.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))


# Joins #
# Build a statement to select the census and state_fact tables
stmt = select([census, state_fact])

# Add a select_from clause that wraps a join for the census and state_fact
# tables where the census state column and state_fact name column match
stmt = stmt.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))

# Execute the statement and get the first result
result = con.execute(stmt).first()

# Loop over the keys in the result object and print the key and value
for key in result.keys():
    print(key, getattr(result, key))


# More Joins #
# Build a statement to select the state, sum of 2008 population and census division name
stmt = select([
    census.columns.state,
    func.sum(census.columns.pop2008),
    state_fact.columns.census_division_name
])

# Append select_from to join the census and state_fact tables by the census state and state_fact name columns
stmt = stmt.select_from(census.join(state_fact, census.columns.state == state_fact.columns.name))

# Append a group by for the state_fact name column
stmt = stmt.group_by(state_fact.columns.name)

# Execute the statement and get the results: results
results = con.execute(stmt).fetchall()

# Loop over the the results object and print each record.
for record in results:
    print(record)


# Hierarchical Tables #
# Define table
engine_empl = create_engine('sqlite:///employees.sqlite')
con_empl = engine_empl.connect()
metadata_empl = MetaData()
employees = Table('employees', metadata_empl, autoload=True, autoload_with=con_empl)

# Make an alias of the employees table
managers = employees.alias()

# Build a query to select manager's and their employees names
stmt = select(
    [managers.columns.name.label('manager'),
     employees.columns.name.label('employee')]
)

# Match managers id with employees mgr
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Order the statement by the managers name
stmt = stmt.order_by(managers.columns.name)

# Execute statement
results = con_empl.execute(stmt).fetchall()

# Print records
for record in results:
    print(record)


# Hierarchical Tables with Functions and Grouping
# Build a query to select managers and counts of their employees
stmt = select([managers.columns.name, func.count(employees.columns.id)])

# Append a where clause that ensures the manager id and employee mgr are equal
stmt = stmt.where(managers.columns.id == employees.columns.mgr)

# Group by Managers Name
stmt = stmt.group_by(managers.columns.name)

# Execute statement
results = con_empl.execute(stmt).fetchall()

# print manager
for record in results:
    print(record)


# Large ResultSets #
# Prepare variables
stmt = select([census])
results_proxy = con.execute(stmt)
state_count = {}
more_results = True

# Start a while loop checking for more results
while more_results:
    # Fetch the first 50 results from the ResultProxy
    partial_results = results_proxy.fetchmany(50)

    # if empty list, set more_results to False
    if partial_results == []:
        more_results = False

    # Loop over the fetched records and increment the count for the state
    for row in partial_results:
        if row.state in state_count:
            state_count[row.state] += 1
        else:
            state_count[row.state] = 1

# Close the ResultProxy, and thus the connection
results_proxy.close()

# Print the count by state
print(state_count)
