import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Downloads\Dataset_Ques_1_4.csv")
print(df.head())

# ----------- GRAPH 1: Total Profit ----------- #
plt.figure(figsize=(10, 5))

plt.plot(df["month_number"], df["total_profit"],
         linestyle='dashed', color='green', linewidth=2,
         label="Total Profit")

plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit Per Month")
plt.legend(loc="lower right")
plt.xticks(rotation=45)
plt.grid(True)

plt.show()


# ----------- GRAPH 2: Toothpaste Sales ----------- #
plt.figure(figsize=(10, 5))

plt.bar(df["month_number"], df["toothpaste"], color='blue')

plt.xlabel("Month")
plt.ylabel("Toothpaste Sales")
plt.title("Toothpaste Sales Per Month")
plt.xticks(rotation=45)
plt.yticks(rotation=30)
plt.grid(axis='y')

plt.show()