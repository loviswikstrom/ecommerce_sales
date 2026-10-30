import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import FuncFormatter

def plot_revenue_by_category(data):
    df = (
        data.groupby("category", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue",ascending=False)
    )

    fig, ax = plt.subplots(figsize=(10, 6), constrained_layout=True)
    ax.bar(df["category"], df["revenue"])
    ax.set_title("Intäkt per kategori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Intäkt (kr)")
    return fig

def plot_revenue_by_city(data):
    rev=data.groupby("city")["revenue"].sum().sort_values()
    fig,ax = plt.subplots(figsize=(10,6))
    ax.barh(rev.index,rev.values)
    ax.set_title("Intäkt per stad")
    ax.set_xlabel("Intäkt (kr)")
    ax.set_ylabel("Stad")

    return fig

def plot_revenue_over_time(data, period="month"):
    if period not in ("month", "week"):
        raise ValueError("period måste vara 'month' eller 'week'")

    data_temp = data.copy()
    data_temp["date"] = pd.to_datetime(data_temp["date"])

    if period == "month":
        data_temp["period"] = data_temp["date"].dt.month
        ticks = range(1, 13)
        label = "månad Januari-Juni 2024"
    else:
        data_temp["period"] = data_temp["date"].dt.isocalendar().week.astype(int)
        ticks = range(1, 54, 4)
        label = "vecka 1-26 2024"

    rev = data_temp.groupby("period")["revenue"].sum().sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(rev.index, rev.values, marker="o")
    ax.set_xticks(rev.index if period == "month" else rev.index[::4])
    ax.set_xlim(rev.index.min(), rev.index.max())
    ax.set_title(f"Revenue per {label}")
    ax.set_xlabel(label.capitalize())
    ax.set_ylabel("Revenue")
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def plot_city_over_time(data):
    data_temp = data.copy()
    data_temp["date"] = pd.to_datetime(data_temp["date"])
    revenue = data_temp.groupby(
        [pd.Grouper(key="date", freq="MS"), "city"]
    )["revenue"].sum().unstack(fill_value=0).sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    for city in revenue.columns:
        ax.plot(revenue.index, revenue[city], marker="o", label=city)
    ax.set_title("Intäkt per stad över tid")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (kr)")
    if len(revenue.columns):
        ax.legend(title="Stad")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    return fig

def plot_category_over_time(data):
    data_temp = data.copy()
    data_temp["date"] = pd.to_datetime(data_temp["date"])
    revenue = data_temp.groupby(
        [pd.Grouper(key="date", freq="MS"), "category"]
    )["revenue"].sum().unstack(fill_value=0).sort_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    for category in revenue.columns:
        ax.plot(revenue.index, revenue[category], marker="o", label=category)
    ax.set_title("Intäkt per kategori över tid")
    ax.set_xlabel("Månad")
    ax.set_ylabel("Intäkt (kr)")
    if len(revenue.columns):
        ax.legend(title="Kategori")
    ax.grid(True, alpha=0.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    return fig

def plot_order_value_dist(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data["revenue"].dropna(), bins=30, edgecolor="black")
    ax.set_title("Fördelning av ordervärden")
    ax.set_xlabel("Ordervärde (kr)")
    ax.set_ylabel("Antal order")
    ax.grid(axis="y", alpha=0.3)
    fig.tight_layout()
    return fig

