import pandas as pd 
data=pd.read_excel("superstore.xls")
data["Year"]=data["Order Date"].dt.year 
YearlySales=data.groupby("Year")["Sales"].sum()
print(YearlySales.sort_values(ascending=False).head(10))
data["Month"]=data["Order Date"].dt.month
monthly_trend=data.groupby(["Year","Month"])["Sales"].sum()
print(monthly_trend.sort_values(ascending=False).head(10))
west_data=data[data["Region"]=="West"]
# sub_category_sales=west_data.groupby("Sub-Category")["Sales"].sum()
# print(sub_category_sales.sort_values())
segment_sales=west_data.groupby("Segment")["Sales"].sum()
print(segment_sales.sort_values(ascending=False))