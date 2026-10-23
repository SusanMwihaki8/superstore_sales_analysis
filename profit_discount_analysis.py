import pandas as pd 
import matplotlib.pyplot as plt  
data=pd.read_excel("superstore.xls")
discount_analysis=data.groupby("Discount").agg(Total_sales=("Sales","sum"),
Total_profit=("Profit","sum"),Average_profit=("Profit","mean"),No_of_Orders=("Order ID","count"))
print(discount_analysis.sort_values("Total_profit"))
category_profit=data.groupby("Category")["Profit"].sum()
fig, axes=plt.subplots(1,2,figsize=(8,4))
axes[0].bar(discount_analysis.index.astype(str),discount_analysis["Average_profit"])
axes[0].set_title("Average profit by Discount level")
axes[0].set_xlabel("Discount")
axes[0].set_ylabel("Average profit")
axes[0].axhline(y=0, linestyle="--")

axes[1].scatter(data["Discount"],data["Profit"])
axes[1].set_title("Profit vs Discount")
axes[1].set_xlabel("Discount")
axes[1].set_ylabel("Profit")
axes[1].axhline(y=0)
plt.tight_layout()

plt.savefig("Discount_profit_analysis.png")
plt.show()