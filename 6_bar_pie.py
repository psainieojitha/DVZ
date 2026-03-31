import pandas as pd
import matplotlib.pyplot as plt

# ----------- PIE CHART (MANUAL DATA) ----------- #
subjects = ['DSC', 'OOP', 'OPS', 'COA', 'MAT', 'JAVA']
pass_percentage = [40, 25.6, 8.8, 30, 7.7, 60.7]
explode = [0, 0, 0, 0, 0, 0.1]

plt.figure(figsize=(7, 7))
plt.pie(pass_percentage,
        labels=subjects,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        shadow=True)

plt.title("Pass Percentage of Subjects")
plt.show()


# ----------- HISTOGRAM ----------- #
df = pd.read_csv(r"C:\Users\Admin\Downloads")
print(df.columns)

profit_data = df['total_profit']

plt.figure(figsize=(7, 5))   # ✅ fixed
plt.hist(profit_data,
         bins=10,
         color='blue',
         edgecolor='black',
         alpha=0.7)

plt.xlabel("Profit Ranges")
plt.ylabel("Frequency")
plt.title("Histogram of Monthly Profits")
plt.show()


# ----------- PIE CHART (FROM CSV) ----------- #
df2 = pd.read_csv(r"C:\Users\Admin\Downloads\New Microsoft Excel Worksheet (2).csv")

subjects = df2['subjects']
pass_percentage = df2['pass_percentage']

max_pass = pass_percentage.max()

explode = [0.1 if val == max_pass else 0 for val in pass_percentage]

plt.figure(figsize=(7, 7))
plt.pie(pass_percentage,
        labels=subjects,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        shadow=True)

plt.title("Pass Percentage of Subjects (From CSV)")
plt.show()