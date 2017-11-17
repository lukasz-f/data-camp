import numpy as np
import matplotlib.pyplot as plt

# Set the seed
np.random.seed(101)


def takeRandomWalk():
    # Initialize random_walk
    random_walk = [0]

    # Complete the random walk
    for x in range(100) :
        # Set step: last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            # Use max to make sure step can't go below 0
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # append next_step to random_walk
        random_walk.append(step)

    return random_walk


# Take a random walk
walk = takeRandomWalk()

# Visualize random walk
plt.plot(walk)
plt.title('Visualize random walk');
plt.show()

# Initialize all_walks
all_walks=[]

# Simulate random walk 10000 times
for i in range(10000) :
    # Take a random walk
    walk = takeRandomWalk()

    # Append random_walk to all_walks
    all_walks.append(walk)

# Visualize all walks
np_aw_t = np.array(all_walks).T
plt.plot(np_aw_t)
plt.title('Visualize all walks');
plt.show()

# Select last row from np_aw_t
ends = np_aw_t[-1]

# Plot the distribution, display plot
plt.hist(ends, bins=25)
plt.title('Random walk distribution')
plt.show()
