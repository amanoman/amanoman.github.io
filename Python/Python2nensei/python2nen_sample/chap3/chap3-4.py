import pandas as pd

# CSVファイルを読み込む
df = pd.read_csv("test.csv")

# 1行のデータを表示
print("C子のデータ\n",df.loc[2])

# 複数の行のデータを表示
print("C子とD郎のデータ\n",df.loc[[2,3]])

# 指定した行の指定した列のデータ
print("C子の国語データ\n", df.loc[2]["国語"])
