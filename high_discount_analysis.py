import pandas as pd 
import matplotlib.pyplot as plt 
data=pd.read_excel("superstore.xls")
high_discount=data[data["Discount"]>=0.50]
category_loss=high_discount.groupby("Category").agg(Total_profit=("Profit","sum"), Total_sales=("Sales","sum"),No_of_orders=("Order ID","count"))
print(category_loss.sort_values("Total_profit"))
office_highdiscount=data[(data["Discount"]>=0.50) ]
product_loss=office_highdiscount.groupby("Sub-Category").agg(Total_Profit=("Profit","sum"),Total_sales=("Sales","sum"),No_of_Orders=("Order ID","count"),Average_profit=("Profit","mean"))
print(product_loss.sort_values("Total_Profit"))
binders=data[(data["Sub-Category"]=="Binders")]
binder_discount=binders.groupby("Discount").agg(Total_sales=("Sales","sum"),Total_profit=("Profit","sum"),No_of_Orders=("Order ID","count"),Average_profit=("Profit","mean"))
print(binder_discount.sort_values("Total_profit"))
plt.bar(binder_discount.index.astype(str), binder_discount["Average_profit"])
plt.axhline(y=0,color="red")
plt.title("Binders' Average profit by discount levels")
plt.xlabel("Discount levels")
plt.ylabel("Average profit")
plt.savefig("binders_analysis.png")
plt.show()

