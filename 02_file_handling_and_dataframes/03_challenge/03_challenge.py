# 必要なライブラリをインポートする
import pandas as pd
from sklearn import datasets

# アイリスのデータセットを読み込み、DataFrameに変換する
iris = datasets.load_iris()
iris_df = pd.DataFrame(iris.data, columns=iris.feature_names)

# 品種の列を追加し、0～2の番号を記入する (各番号が異なる品種を表す)
iris_df['species'] = iris.target

# データの概要を表示する
print("データの最初の5行:\n", iris_df.head())

# 欠損値またはnull値の存在を確認する
print("\n欠損値の存在確認:\n", iris_df.isnull().sum())

# 各列のデータ型を確認する
print("\n各列のデータ型:\n", iris_df.dtypes)

# 基本統計量の計算
statistics_df = iris_df.describe().T[['mean', '50%', 'std']]
statistics_df.columns = ['mean', 'median', 'std']

# ガクの面積 (sepal_area) の計算
iris_df['sepal_area'] = iris_df['sepal length (cm)'] * iris_df['sepal width (cm)']

# 花弁の面積 (petal_area) の計算
iris_df['petal_area'] = iris_df['petal length (cm)'] * iris_df['petal width (cm)']

# 新しい特徴量の基本統計量を計算
additional_stats = iris_df[['sepal_area', 'petal_area']].describe().T[['mean', '50%', 'std']]
additional_stats.columns = ['mean', 'median', 'std']

# 既存の統計情報に新しい特徴量の統計情報を追加する
statistics_df = pd.concat([statistics_df, additional_stats])

# 統計情報をCSV形式で出力する
statistics_df.to_csv('iris_statistics.csv')

# データのフィルタリング関数を定義する (例: ある列の値がしきい値を下回る行を除外する)
def filter_data(df, column, threshold):
    return df[df[column] >= threshold]

# 例として、花弁の長さが1.5cm以上のデータのみを残す
filtered_iris_df = filter_data(iris_df, 'petal length (cm)', 1.5)

# フィルタリングされたデータをCSV形式で保存する
filtered_iris_df.to_csv('filtered_iris_data.csv', index=False)

# 生成されたDataFrameとCSVファイルを確認するための出力を行う
print("\n統計情報を含むDataFrame:\n", statistics_df)
print("\nフィルタリングされたデータの最初の5行:\n", filtered_iris_df.head())
