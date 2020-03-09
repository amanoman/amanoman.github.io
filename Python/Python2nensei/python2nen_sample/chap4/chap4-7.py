import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

# データフレームを読み込む
df = pd.read_csv("FEH_00200524_190618234018.csv", index_col="全国・都道府県", encoding="shift_jis")

# 平成30年の列データで棒グラフを作って表示する
df = df.drop("全国", axis=0)
df["平成30年"] = pd.to_numeric(df["平成30年"].str.replace(",", ""))
df["平成30年"].plot.bar(figsize=(10, 6))
plt.show()