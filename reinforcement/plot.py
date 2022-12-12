import matplotlib.pyplot as plt
import math
# set up parameters
epsilon_min = 0
epsilon_max = 1
decay_rate = 0.05  # chosen based on the specific task

# compute epsilon values for each episode
num_episodes = 100
epsilons = []
for i in range(num_episodes):
    epsilons.append(epsilon_min + (epsilon_max - epsilon_min) * math.exp(-decay_rate * i))

# plot epsilon values over episodes
plt.plot(range(num_episodes), epsilons)
plt.xlabel('Episode')
plt.ylabel('Epsilon')
plt.show()
