import matplotlib.pyplot as plt

def plot_revenue_by_category(data):
    fig,ax = plt.subplots(figsize=(10,6))

    ax.bar(data["category"], data["revenue"])
    ax.set_title("Intäkt per kateogori")
    ax.set_xlabel("Kategori")
    ax.set_ylabel("Intäkt (kr)")

    return fig

def plot_revenue_by_city():
    return None

def plot_revenue_over_time():
    return None

def plot_order_value_dist():
    return None

