
import pandas as pd

df = pd.read_csv("consolidated_data.csv")

# Top country by sales
top_country = df.groupby("Country")["sales_eur"].sum().sort_values(ascending=False)

# Monthly trend
df["Month"] = pd.to_datetime(df["Date"]).dt.to_period("M")
monthly_sales = df.groupby("Month")["sales_eur"].sum()

print(top_country)
print(monthly_sales)
