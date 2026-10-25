import matplotlib.pyplot as plt
import viz
import metrics

class EcommerceAnalyzer:
    """Metoder för att förbereda inför analys för
    de frågor vi vill svar på"""
    def __init__(self, data):
        self.data = data.copy()

    def category_breakdown(self):
        """Skriver ut kategoristatistik och grafer"""
        table = metrics.category_revenue_table(self.data)
        print(table.round(2).to_string(index=False))
        viz.plot_revenue_by_category(self.data)
        plt.show()
        return table

    
        