# Import necessary module
from sqlalchemy import create_engine
import pandas as pd

# Create engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)

# Open engine connection
con = engine.connect()

# Perform query
rs = con.execute('select * from Album')

# Save results of the query to DataFrame
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())


# Customizing SQL Queries #
# Open engine in context manager
# Perform query and save results to DataFrame
with engine.connect() as con:
    rs = con.execute('select LastName, Title from Employee')
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())


# Filtering your database records using SQL's WHERE #
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('select * from Employee where EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())


# Ordering your SQL records with ORDER BY #
# Open engine in context manager
with engine.connect() as con:
    rs = con.execute('select * from Employee order by BirthDate')
    df = pd.DataFrame(rs.fetchall())

    # Set the DataFrame's column names
    df.columns = rs.keys()

# Print head of DataFrame
print(df.head())


# Pandas and SQL Queries #
# Execute query and store records in DataFrame
df = pd.read_sql_query('select * from Album', engine)

# Print head of DataFrame
print(df.head())


# Pandas for more complex querying #
# Execute query and store records in DataFrame
df = pd.read_sql_query('select * from Employee where EmployeeId >= 6 order by BirthDate', engine)

# Print head of DataFrame
print(df.head())


# The power of SQL: INNER JOIN #
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('select Album.Title, Artist.Name from Album inner join Artist on Artist.ArtistId = Album.ArtistId')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())


# Filtering your INNER JOIN #
# Execute query and store records in DataFrame
df = pd.read_sql_query('select * from PlaylistTrack inner join Track on PlaylistTrack.TrackId = Track.TrackId where Track.Milliseconds < 250000', engine)

# Print head of DataFrame
print(df.head())
