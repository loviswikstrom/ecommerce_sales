import pandas as pd
import numpy as np

"""df = pd.read_csv("data/ecommerce_sales.csv")"""


# 1. total intäkt
def revenue_sum(data):
    total = round(data["revenue"].sum(), 2)
    return total

# 2. totalt antal enheter.
def units_sum(data):
    units_total = data["units"].sum()
    return units_total


# 3. Average Orde Value (aov)
def aov(data):
    total_revenue = data["revenue"].sum()
    total_orders = data["order_id"].nunique()
    average = round(total_revenue / total_orders, 2)
    return average


# 4. intäkt per kategori.
def category_revenue_table(data):
    category_revenue = (
    data.groupby("category")["revenue"]
    .agg(
        kronor = "sum",
        count = "count",
        mean = "mean",
        median = "median",
        std = "std"
    )
    .reset_index()
    )  
    return category_revenue


# 5. intäkt per stad.
def city_revenue(data):
    city_revenue = (
        data.groupby("city")["revenue"]
        .agg(kronor = "sum", count = "count", mean = "mean", median = "median", std = "std")
        .reset_index()
    )
    return city_revenue


# 6. top 3 kategorier efter intäkt.
def top_category_revenue(data):
    category_revenue = category_revenue_table(data)
    top_category = category_revenue.sort_values("kronor", ascending=False).head(3)
    return top_category



# 7. högst genomsnittligt ordervärde per stad
def aov_per_city(data):
    city_orders = data.groupby("city")["order_id"].nunique()
    city_revenue = data.groupby("city")["revenue"].sum()

    aov_per_city = city_revenue / city_orders
    aov_per_city = aov_per_city.sort_values(ascending=False)
    return aov_per_city