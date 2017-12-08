# Import packages
import pandas as pd


# Importing non-flat files from the web #
# Assign url of file
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Read in all sheets of Excel file
xl = pd.read_excel(url, sheetname=None)

# Print xl type
print(type(xl))

# Print the sheetnames to the shell
print(xl.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xl['1700'].head())
