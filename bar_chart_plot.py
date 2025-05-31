import matplotlib.pyplot as plt

# Sample data
gender_counts = {
    'Male': 55,
    'Female': 45
}

# Data for the bar chart
labels = list(gender_counts.keys())
values = list(gender_counts.values())

plt.bar(labels, values, color=['steelblue', 'salmon'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
