import pandas as pd
import re

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
print(df)
#df.to_csv("dist\\test_20221109.csv")