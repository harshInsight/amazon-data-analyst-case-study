Loading Excel Files
import pandas as pd

df_de = pd.read_excel("Germany.xlsx")
df_fr = pd.read_excel("France.xlsx")
df_es = pd.read_excel("Spain.xlsx")
df_uk = pd.read_excel("UK.xlsx")
df_us = pd.read_excel("US.xlsx")

Date Standardization

df_de["Date"] = pd.to_datetime(df_de["Date"], errors="coerce")
Remove Duplicates & Nulls

df_de.drop_duplicates(inplace=True)
df_de.dropna(subset=["Order ID"], inplace=True)

Currency Conversion to EURO
exchange_rates = {
    "EUR": 1,
    "USD": 0.93,
    "GBP": 1.17
}

df_de["sales_eur"] = df_de.apply(
    lambda x: x["Sales"] * exchange_rates[x["Currency"]],
    axis=1
)
Dataset Consolidation

final_df = pd.concat([df_de, df_fr, df_es, df_uk, df_us], ignore_index=True)

Top Country by Sales
final_df.groupby("Country")["sales_eur"].sum().sort_values(ascending=False)

Monthly Trend

final_df["Month"] = final_df["Date"].dt.to_period("M")
final_df.groupby("Month")["sales_eur"].sum()


Refund Analysis
refund_rate = final_df.groupby("SKU")["Refund Amount"].mean()
