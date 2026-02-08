import pandas as pd

# Load Excel files
df_de = pd.read_excel("Germany.xlsx")
df_fr = pd.read_excel("France.xlsx")
df_es = pd.read_excel("Spain.xlsx")
df_uk = pd.read_excel("UK.xlsx")
df_us = pd.read_excel("US.xlsx")

datasets = [df_de, df_fr, df_es, df_uk, df_us]

# Standardize & clean
for df in datasets:
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df.drop_duplicates(inplace=True)
    df.dropna(subset=["Order ID"], inplace=True)

# Currency conversion
exchange_rates = {
    "EUR": 1,
    "USD": 0.93,
    "GBP": 1.17
}

for df in datasets:
    df["sales_eur"] = df.apply(
        lambda x: x["Sales"] * exchange_rates.get(x["Currency"], 1),
        axis=1
    )

# Merge all countries
final_df = pd.concat(datasets, ignore_index=True)
final_df.to_csv("consolidated_data.csv", index=False)
