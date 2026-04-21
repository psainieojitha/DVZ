import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('titanic')

# ------------------ SCATTER PLOTS ------------------
fig, axes = plt.subplots(2, 1, figsize=(10, 10))

sns.scatterplot(data=df, x='age', y='fare', hue='survived', ax=axes[0])
axes[0].set_title('Scatter Plot - Age vs Fare')

sns.scatterplot(data=df, x='age', y='pclass', hue='sex', ax=axes[1])
axes[1].set_title('Scatter Plot - Age vs Pclass')

plt.tight_layout()
plt.show()

# ------------------ VIOLIN PLOT (FIXED) ------------------
sns.violinplot(data=df, x='pclass', y='age', hue='sex', split=True)

plt.title('Violin Plot of Age by Passenger Class and Sex')
plt.xlabel('Passenger Class')
plt.ylabel('Age')

plt.show()

# ------------------ LINE PLOT ------------------
survival_data = df.groupby(['pclass', 'survived']).size().reset_index(name='count')

sns.lineplot(data=survival_data, x='pclass', y='count', hue='survived', marker='o')

plt.title('Passenger Survival Count by Class')
plt.xlabel('Passenger Class')
plt.ylabel('Passengers')

plt.show()

# ------------------ STRIP PLOT ------------------
sns.stripplot(data=df, x='sex', y='age', jitter=False, hue='survived', palette='Set2')

plt.title('Strip Plot of Age by Sex (No Jitter)')
plt.xlabel('Sex')
plt.ylabel('Age')

plt.show()