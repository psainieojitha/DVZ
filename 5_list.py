import numpy as np
import matplotlib.pyplot as plt

# sample data
categories = ['A','B','C','D','E']
means_men = [22,30,35,35,26]
means_women = [25,32,30,35,29]

bar_width = 0.5

# stacked bars
plt.bar(categories, means_men, width=bar_width, label='Men', color='skyblue')
plt.bar(categories, means_women, width=bar_width, bottom=means_men, label='Women', color='pink')

# labels and title
plt.xlabel("Categories")
plt.ylabel("Means")
plt.yticks(np.arange(0, 81, 10))
plt.title("Score by Group and Gender")

# adding values inside bars
for i in range(len(categories)):
    # Men (middle of first bar)
    plt.text(i, means_men[i]/2, str(means_men[i]),
             ha='center', va='center', fontweight='bold')
    
    # Women (middle of stacked part)
    plt.text(i, means_men[i] + means_women[i]/2, str(means_women[i]),
             ha='center', va='center', fontweight='bold')

plt.legend()
plt.show()