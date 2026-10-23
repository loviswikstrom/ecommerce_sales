import pandas as pd
import numpy as np

df = pd.read_csv("data/ecommerce_sales.csv")


# 1. total intäkt och totalt antal enheter.
revenue_sum = df["revenue"].sum().round(2)
print("Total intäkt:", revenue_sum, "kronor")

units_sum = df["units"].sum()
print("Totalt sålda enheter:", units_sum, "styck")


# 2. Average Orde Value (aov)
aov = revenue_sum / df["units"].count()
print("Genomsnittligt värde per order är: ", aov.round(2), "kronor")


# 3. intäkt per kategori.
category_revenue = (
    df.groupby("category")["revenue"]
    .agg(kronor = "sum", count = "count", mean = "mean", median = "median", std = "std")
    .reset_index()
)
category_revenue


# 4. intäkt per stad.
city_revenue = (
    df.groupby("city")["revenue"]
    .agg(kronor = "sum", count = "count", mean = "mean", median = "median", std = "std")
    .reset_index()
)
city_revenue


# 5. top 3 kategorier efter intäkt.
category_revenue.sort_values("kronor", ascending=False).head(3)