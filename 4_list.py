import matplotlib.pyplot as plt
import numpy as np

languages = ['Fict','Tech','Moti','Business','Nutri','Dev']
sales = [5.2, 19.6, 8.7, 7.7, 3.7, 6.5]
colors = ['#1f77b4','#ff7f0e','#2ca02c','#d62728','#9467bd','#8c564b']

plt.barh(languages, sales, color=colors)

plt.xlabel("Sales (in million)")
plt.ylabel("Book Categories")
plt.title("Book Sales by Category")

plt.xticks(np.arange(0, 25, 5))
plt.yticks(languages)

plt.legend(["Book Sales"], loc='upper right')
plt.tight_layout()
plt.savefig('book_sales_horizontal_bar.png')
plt.show()