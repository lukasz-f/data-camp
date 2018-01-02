from sqlalchemy import create_engine

# Create an engine to the census database
engine = create_engine('sqlite:///census.sqlite')

# Print the table names
print(engine.table_names())
