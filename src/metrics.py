import pandas as pd
import numpy as np

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
        antal = "count",
        medelvärde = "mean",
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
        .agg(
            kronor = "sum",
            antal = "count",
            medelvärde = "mean",
            median = "median",
            std = "std"
            )
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


# 8. översikt över intäkt
def revenue_overview(data):
    median = data["revenue"].median()
    minsta = data["revenue"].min()
    hogsta = data["revenue"].max()
    standardavvikelse = data["revenue"].std()

    print("Median:", round(median, 2), "kronor")
    print("Lägsta ordervärde:", round(minsta, 2), "kronor")
    print("Högsta ordervärde:", round(hogsta, 2), "kronor")
    print("Standardavvikelse:", round(standardavvikelse, 2), "kronor")


# 9. avvikelser
def outliers_category(data):
    category_revenue = data.groupby("category")["revenue"].sum()
    return category_revenue


def outliers_month(data):
    data["date"] = pd.to_datetime(data["date"])
    data["month"] = data["date"].dt.to_period("M")
    revenue_per_month = data.groupby("month")["revenue"].sum()
    return revenue_per_month


def outliers_order(data):
    order = round(data["revenue"], 2)
    return order