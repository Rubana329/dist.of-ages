import matplotlib.pyplot as plt
import numpy as np

# Sample data: ages of 100 people
ages = np.random.randint(18, 70, size=100)

plt.hist(ages, bins=10, color='skyblue', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
