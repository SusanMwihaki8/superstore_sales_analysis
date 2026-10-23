import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns
data=pd.read_excel("superstore.xls")
correlation=data[["Sales","Profit","Quantity","Discount"]].corr()
sns.heatmap(correlation, annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()