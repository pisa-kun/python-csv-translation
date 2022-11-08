import pandas as pd
import re
import mojimoji

file = 'src\\test_0001_20221109.csv'
df = pd.read_csv(file, header=0)
print(df)

# searchできない場合はm.groupで例外発生
m = re.search(r'\d{4}', file)
f = m.group()

m2 = re.search(r'\d{8}', file)
t = m2.group()

# フォーマットの追加
# 先頭に追加
df.insert(0, "format", f)
# 日付の追加
# 2行目に追加
df.insert(1, "time", t) 

# CF, FZのみ抜き出し
isModel = df['serial'].str.startswith(("CF", "FZ"))
df2 = df[isModel]
print(df2)

# memoフィールドの英数字を全角から半角に
memo = df2["memo"]
print(memo)

# df型は列番号をもつので、indexは無視する
df2.to_csv("dist\\test_20221109.csv", index=False)