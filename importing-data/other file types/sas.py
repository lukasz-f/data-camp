# Import sas7bdat package
from sas7bdat import SAS7BDAT
import pandas as pd
import matplotlib.pyplot as plt

# Save file to a DataFrame
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
