import pandas as pd

df = pd.read_csv('src\\test_0001_20221109.csv', header=0)
print(df)

# フォーマットの追加
df["format"] = "1000"
# 日付の追加
df["time"] = "20220425"
print(df)
#df.to_csv("dist\\test_20221109.csv")