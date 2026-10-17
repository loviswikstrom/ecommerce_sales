import matplotlib.pyplot as plt

def plot_revenue_by_category(data):
    fig,ax = plt.subplots(figsize=(10,6))

    ax.bar(data["category"], data["revenue"])
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

def plot_revenue_over_time():
    return None

def plot_order_value_dist():
    return None

