import pandas as pd
df = pd.read_csv("retail_sales.csv")

print(df.head(5))
print(df.tail(5))
print(df.columns)
print(df.shape)

df["Date"]=pd.to_datetime(df["Date"])
df['Year']=df["Date"].dt.year
df['Month']=df["Date"].dt.month
df["Day"]=df["Date"].dt.day
print(df.head(5))

print(df.groupby("City")["TotalPrice"].sum())
print(df.groupby("Store")["TotalPrice"].sum())
print(df.groupby("Category")["TotalPrice"].sum())

print(df.sort_values("TotalPrice", ascending=False).head(5))


Electronics = df[(df["Category"] == "Electronics") & (df["Quantity"] > 1)]
print(Electronics)

df["Discount"]=