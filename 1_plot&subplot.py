import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\Downloads\Dataset_Ques_1_4.csv")

months = df['month_number']
total_profit = df['total_profit']
bathing_soap_sales = df['bathingsoap']
facewash_sales = df['facewash']

# ----------- GRAPH 1: Total Profit ----------- #
plt.figure(figsize=(10, 5))

plt.plot(months, total_profit, linestyle='dotted', color='green', marker='s', label='Total Profit')

# Add annotation for each point
for i, txt in enumerate(total_profit):
    plt.annotate(txt, (months[i], total_profit[i]),
                 textcoords="offset points", xytext=(0, 5), ha='center')

plt.xlabel('Month')
plt.ylabel('Total Profit')
plt.title('Total Profit per Month')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.show()


# ----------- GRAPH 2: Subplots ----------- #
fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Bathing Soap
axes[0].plot(months, bathing_soap_sales, marker='o', linestyle='-', color='blue', label='Bathing Soap Sales')

for i, txt in enumerate(bathing_soap_sales):
    axes[0].annotate(txt, (months[i], bathing_soap_sales[i]),
                     textcoords="offset points", xytext=(0, 5), ha='center')

axes[0].set_title('Bathing Soap Sales per Month')
axes[0].set_ylabel('Sales')
axes[0].legend()
axes[0].grid(True)


# Facewash
axes[1].plot(months, facewash_sales, marker='o', linestyle='-', color='red', label='Facewash Sales')

for i, txt in enumerate(facewash_sales):
    axes[1].annotate(txt, (months[i], facewash_sales[i]),
                     textcoords="offset points", xytext=(0, 5), ha='center')

axes[1].set_title('Facewash Sales per Month')
axes[1].set_xlabel('Month')
axes[1].set_ylabel('Sales')
axes[1].legend()
axes[1].grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()