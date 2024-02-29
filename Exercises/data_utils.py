import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ritar ett stapeldiagram för kolumner med saknade värden i en DataFrame.
def plot_missing_values(df):
    
    # Räkna saknade värden per kolumn
    missing_values = df.isnull().sum()
    missing_values = missing_values[missing_values > 0]

    # Om det finns saknade värden, rita ett stapeldiagram
    if not missing_values.empty:
        sns.barplot(x=missing_values.index, y=missing_values.values)
        plt.ylabel('Antal saknade värden')
        plt.xticks(rotation=45, ha='right')
        plt.title('Saknade värden per kolumn')
        plt.show()
    else:
        print("Inga saknade värden hittades.")
