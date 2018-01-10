from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, String, Integer, Float, Boolean
from sqlalchemy import insert, select
from sqlalchemy import update
from sqlalchemy import delete
from sqlalchemy import func
from sqlalchemy import and_
import csv

engine = create_engine('sqlite:///:memory:')
con = engine.connect()
metadata = MetaData()

# Creating Tables #
# Define a new table with a name, count, amount, and valid column
data = Table('data', metadata,
             Column('name', String(255), unique=True),
             Column('count', Integer(), default=1),
             Column('amount', Float()),
             Column('valid', Boolean(), default=False))

# Use the metadata to create the table
metadata.create_all(engine)

# Print table details
print(repr(data))
print(repr(metadata.tables['data']))

# Print constraints and defaults
print(data.constraints)


# Inserting a single row #
# Build an insert statement to insert a record into the data table
stmt = insert(data).values(name='Anna', count=1, amount=1000.00, valid=True)

# Execute the statement via the connection: results
results = con.execute(stmt)

# Print result rowcount
print(results.rowcount)

# Build a select statement to validate the insert
stmt = select([data]).where(data.columns.name == 'Anna')

# Print the result of executing the query.
print(con.execute(stmt).first())


# Inserting Multiple Records #
# Build a list of dictionaries
values_list = [
    {'name': 'Maria', 'count': 1, 'amount': 1000.00, 'valid': True},
    {'name': 'Taylor', 'count': 1, 'amount': 750.00, 'valid': False}
]

# Build an insert statement for the data table
stmt = insert(data)

# Execute stmt with the values_list
results = con.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)


# Loading a CSV into a Table #
census = Table('census', metadata,
               Column('state', String(length=30)),
               Column('sex', String(length=1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()))
metadata.create_all(engine)

# Create a insert statement for census
stmt = insert(census)

# Create an empty list and zeroed row count
values_list = []
total_rowcount = 0

# Create csv reader
f = open('census.csv')
csv_reader = csv.reader(f)

# Enumerate the rows of csv_reader
for idx, row in enumerate(csv_reader):
    # create data and append to values_list
    values = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
    values_list.append(values)

    # Check to see if divisible by 51
    if idx % 51 == 0:
        results = con.execute(stmt, values_list)
        total_rowcount += results.rowcount
        values_list = []

# Print total rowcount
print(total_rowcount)
f.close()


# Updating individual records #
# Create an engine to the census database
engine_cens = create_engine('sqlite:///census.sqlite')
con_cens = engine_cens.connect()
metadata_cens = MetaData()
state_fact = Table('state_fact', metadata_cens, autoload=True, autoload_with=engine_cens)

# Build a select statement
select_stmt = select([state_fact]).where(state_fact.columns.name == 'New York')

# Print the results of executing the select_stmt
print(con_cens.execute(select_stmt).fetchall())

# Build a statement to update the fips_state to 36
stmt = update(state_fact).values(fips_state=36)

# Append a where clause to limit it to records for New York state
stmt = stmt.where(state_fact.columns.name == 'New York')

# Execute the statement
results = con_cens.execute(stmt)

# Print rowcount
print(results.rowcount)

# Execute the select_stmt again to view the changes
print(con_cens.execute(select_stmt).fetchall())


# Updating Multiple Records #
# Build a statement to update the notes to 'The Wild West'
stmt = update(state_fact).values(notes='The Wild West')

# Append a where clause to match the West census region records
stmt = stmt.where(state_fact.columns.census_region_name == 'West')

# Execute the statement
results = con_cens.execute(stmt)

# Print rowcount
print(results.rowcount)


# Correlated Updates #
# Prepare flat_census table
flat_census = Table('flat_census', metadata_cens,
                    Column('state_name', String(length=256)),
                    Column('fips_code', String(length=256)))
metadata_cens.create_all(engine_cens)
results = con_cens.execute(insert(flat_census), [{'fips_code': '1'}, {'fips_code': '2'}, {'fips_code': '4'}])
print(results.rowcount)

# Build a statement to select name from state_fact
fips_stmt = select([state_fact.columns.name])

# Append a where clause to Match the fips_state to flat_census fips_code
fips_stmt = fips_stmt.where(state_fact.columns.fips_state == flat_census.columns.fips_code)

# Build an update statement to set the name to fips_stmt
update_stmt = update(flat_census).values(state_name=fips_stmt)

# Execute update_stmt
results = con_cens.execute(update_stmt)

# Print rowcount
print(results.rowcount)


# Deleting specific records #
# Build a statement to count records using the sex column for Men ('M') age 36
stmt = select([func.count(census.columns.sex)]).where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the select statement and use the scalar() fetch method to save the record count
to_delete = con.execute(stmt).scalar()

# Build a statement to delete records from the census table: stmt_del
stmt_del = delete(census)

# Append a where clause to target Men ('M') age 36
stmt_del = stmt_del.where(
    and_(census.columns.sex == 'M',
         census.columns.age == 36)
)

# Execute the statement: results
results = con.execute(stmt_del)

# Print affected rowcount and to_delete record count, make sure they match
print(results.rowcount, to_delete)


# Deleting all the records from a table #
# Build a statement to empty the census table
stmt = delete(census)

# Execute the statement
results = con.execute(stmt)

# Print affected rowcount
print(results.rowcount)

# Build a statement to select all records from the census table
stmt = select([census])

# Print the results of executing the statement to verify there are no rows
print(con.execute(stmt).fetchall())


# Deleting a Table Completely #
# Drop the state_fact table
data.drop(engine)

# Check to see if state_fact exists
print(state_fact.exists(engine))

# Drop all tables
metadata.drop_all(engine)

# Check to see if census exists
print(census.exists(engine))
