import pandas as pd
import re
import mojimoji
import datetime

file = 'src\\test_0001_20221109122531.csv'
df = pd.read_csv(file, header=0)
print(df)

# searchできない場合はm.groupで例外発生
m = re.search(r'\d{4}', file)
f = m.group()

m2 = re.search(r'\d{14}', file)
t = m2.group()

# フォーマットの追加
# 先頭に追加
df.insert(0, "format", f)
# 日付の追加
# 2行目に追加
df.insert(1, "time", datetime.datetime.strptime(t, "%Y%m%d%H%M%S"))

# CF, FZのみ抜き出し
isModel = df['serial'].str.startswith(("CF", "FZ"))

# - 削除
df['serial'] = df[isModel]['serial'].apply(lambda serial: serial.replace('-', ''))

# memoフィールドの英数字を全角から半角に
df['memo'] = df[isModel]['memo'].apply(lambda str: mojimoji.zen_to_han(str, kana=False))
df['memo'] = df[isModel]['memo'].apply(lambda str: mojimoji.han_to_zen(str, ascii=False, digit=False))

# JST to UTC
jst2utc = datetime.timedelta(hours=-9)
df['inputdate'] = df[isModel]['inputdate'].apply(lambda str: (datetime.datetime.strptime(str, "%Y-%m-%d %H:%M:%S.%f") + jst2utc))

# df型は列番号をもつので、indexは無視する
df[isModel].rename(columns=str.upper).to_csv("dist\\test_20221109122531.csv", index=False)