import matplotlib.pyplot as plt
import numpy as np

year = [1950, 2000, 2050, 2100]
pop = [2.53, 6.13, 9.55, 10.85]
# Line plot
plt.plot(year, pop)  # Define horizontal and vertical axis
plt.show()  # Show the plot

year = [1800, 1850, 1900] + year  # Add data to show population explosion
pop = [1.0, 1.262, 1.650] + pop
plt.fill_between(year, pop, 0, color='green')  # Fill up area under the graph
plt.xlabel('Year')  # Label x-axis
plt.ylabel('Population')  # Label y-axis
plt.title('World Population Projections')  # Title plot
plt.xticks([1800, 1900, 2000, 2100])  # Set ticks on y-axis
plt.yticks([0, 2, 4, 6, 8, 10], ['0', '2B', '4B', '6B', '8B', '10B'])  # Set names of ticks on y-axis
plt.show()

# Scatter plot (Dots)
plt.scatter(year, pop)
plt.xscale('log')  # Put x-axis on logarithmic scale
plt.show()

numbers = [0, 0.6, 1.4, 1.6, 2.2, 2.5, 2.6, 3.2, 3.5, 3.9, 4.2, 6]
plt.scatter(year, pop, s=numbers)  # Dots size corresponds to numbers
plt.xscale('log')  # Put x-axis on logarithmic scale
plt.show()

# Histogram
plt.hist(numbers)  # Build a histogram
plt.show()

plt.clf()  # Cleans plot
plt.hist(numbers, bins=3)  # Specify number of bins
plt.show()
