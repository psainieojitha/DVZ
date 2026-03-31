import pandas as pd
import matplotlib.pyplot as plt

# 1. load thedatasets
df = pd.read_csv(r"C:\Users\Admin\Downloads")
product_cols = ['facecream','facewash','toothpaste','bathingsoap','shampoo','moisturizer']
product_sales = df[product_cols].sum()
print(product_cols)
print(product_sales)

#identify hightest sales
max_sale=product_sales.max()
explode_values=[.1 if val==max_sale else 0 for val in product_sales]
sales_labels=[str(int(val))for val in product_sales]
plt.figure(figsize=(10,8))
#labels=sales_labels(to show the numbers)
#labeldistance=.7 (to move the numbers)
plt.pie(
    product_sales,
    labels=sales_labels,
    explode=explode_values,
    startangle=60,
    labeldistance=0.7,
    shadow=True,
    textprops={'weight':'bold','color':'gold'}
)
#plt.show()
#add a legend so we know which color is which product

plt.legend(product_sales.index,title="Products",loc="upper left",bbox_to_anchor=(1,.5))
plt.title("Total Sales Data for Each Product")
plt.axis('equal')
plt.tight_layout()
#plt.show()

#bar chart
plt.figure(figsize=(8,4))
plt.barh(['Face Cream','Face wash'],[df['facecream'].sum(),df['facewash'].sum()],color=['skyblue','orange'])
plt.xlabel("Total Units Sold")
plt.title("Face Cream vs Face Wash Comparison")
plt.show()