import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
df = sns.load_dataset('planets')
print(df)

# Scatter Plot
sns.set_palette("husl")
plt.figure(figsize=(12, 6))

sns.scatterplot(
    data=df,
    x='year',
    y='distance',
    hue='method',
    size='mass',
    sizes=(20, 200),
    alpha=0.7
)

plt.title("Distance vs Year with Method and Mass")
plt.xlabel("Discovery Year")
plt.ylabel("Distance")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Bar Plot

# groupby and convert to dataframe
method_distance = df.groupby('method')['distance'].mean().reset_index()

plt.figure(figsize=(12, 6))

sns.barplot(
    data=method_distance,
    x='method',
    y='distance',
    palette='husl'
)

plt.title("Average Distance by Discovery Method")
plt.xlabel("Discovery Method")
plt.ylabel("Average Distance")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()