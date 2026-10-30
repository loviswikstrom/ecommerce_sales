import pandas as pd
import matplotlib.pyplot as plt
import viz
import metrics

class EcommerceAnalyzer:
    """Metoder för att förbereda inför analys för
    de frågor vi vill svar på"""
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()

    def total_revenue(self) -> pd.DataFrame:
        """Skriver ut total försäljning samt 
        fördelning över månad/vecka"""
        revenue = metrics.revenue_sum(self.data)
        units = metrics.units_sum(self.data)
        print(f"Total intäkt: {revenue}")
        print(f"Antal enheter: {units}")
        viz.plot_revenue_over_time(self.data, "month")
        viz.plot_revenue_over_time(self.data, "week")
        plt.show()

    def average_order_value(self) -> pd.DataFrame:
        """Redovisar för genomsnittligt ordervärde (AOV)"""
        aov = metrics.aov(self.data)
        print("Genomsnittligt ordervärde (AOV):", aov)
        viz.plot_order_value_dist(self.data)
        plt.show()

    def city_breakdown(self) -> pd.DataFrame:
        """Skriver ut statistik och grafer baserat på stad"""
        table = metrics.city_revenue(self.data)
        table = table.rename(columns={"city": "stad"})
        print(table.round(2).to_string(index=False))
        viz.plot_revenue_by_city(self.data)
        viz.plot_city_over_time(self.data)
        plt.show()

    def category_breakdown(self) -> pd.DataFrame:
        """Skriver ut kategoristatistik och grafer"""
        table = metrics.category_revenue_table(self.data)
        table = table.rename(columns={"category": "kategori"})
        print(table.round(2).to_string(index=False))
        viz.plot_revenue_by_category(self.data)
        viz.plot_category_over_time(self.data)
        plt.show()
    
    def top3_categories(self) -> pd.DataFrame:
        """Skriver ut vilka som är de Top-3 kategorierna,
        baserat på intäkt."""
        table = metrics.top_category_revenue(self.data)
        table = table.rename(columns={"category": "kategori"})
        print("Top-3 kategorier:")
        print(table.iloc[:3, :2].round(2).to_string(index=False))