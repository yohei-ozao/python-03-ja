# ここにコードを書いてください
import pandas as pd
from sklearn.datasets import load_wine

wine_data = load_wine()
wine_df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)

print(wine_df.set_index("alcohol").sort_index().head())

print(wine_df[(wine_df["alcohol"]>13) & (wine_df["malic_acid"]>2)])

#print(wine_df.head())