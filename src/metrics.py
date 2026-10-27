import pandas as pd
import numpy as np

df = pd.read_csv("data/ecommerce_sales.csv")


# 1. total intäkt och totalt antal enheter.
revenue_sum = df["revenue"].sum().round(2)
print("Total intäkt:", revenue_sum, "kronor")

#Lovis:
def revenue_sum(data):
    total = data["revenue"].sum().round(2)
    return total



units_sum = df["units"].sum()
print("Totalt sålda enheter:", units_sum, "styck")

#Lovis:
def units_sum(data):
    units_total = data["units"].sum()
    return units_total


# 2. Average Orde Value (aov)
aov = revenue_sum / df["units"].count()
print("Genomsnittligt värde per order är: ", aov.round(2), "kronor")

#Lovis:
def aov(data):
    total_revenue = data["revenue"].sum()
    total_orders = data["order_id"].nunique()
    average = round(total_revenue / total_orders, 2)
    return average


# 3. intäkt per kategori.
def category_revenue_table(data):
    category_revenue = (
    data.groupby("category")["revenue"]
    .agg(kronor = "sum", count = "count", mean = "mean", median = "median", std = "std")
    .reset_index()
    )  
    return category_revenue
 
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

#Lovis
def city_revenue(data):
    city_revenue = (
        data.groupby("city")["revenue"]
        .agg(kronor = "sum", count = "count", mean = "mean", median = "median", std = "std")
        .reset_index()
    )
    return city_revenue


# 5. top 3 kategorier efter intäkt.
category_revenue.sort_values("kronor", ascending=False).head(3)



# 6. högst genomsnittligt ordervärde per stad
def aov_per_city(data):
    city_orders = data.groupby("city")["order_id"].nunique()
    city_revenue = data.groupby("city")["revenue"].sum()
    aov_per_city = city_revenue / city_orders
    aov_per_city = aov_per_city.sort_values(ascending=False)
    return aov_per_city