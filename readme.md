### pythonでcsvを読み込んで色々する

#### 要件
- 特定の列に含まれている *-* を削除する
- ファイル名に含まれているyyyyMMddを列に追加する
- ファイル名に含まれているフォーマットバージョンを列に追加する
- JSTをUTCに変換する
- 特定の列に含まれている文字列の先頭2文字で判定する
- 英数字を半角に変換する
- 半角カタカナは全角に変換する

日付時刻はnavie　時差情報tzinfoをもたない

#### 時刻の計算
**timedeltaオブジェクトはdatetimeオブジェクトやdateオブジェクトと引き算や足し算などの演算が可能。例えば、1週間前とか10日後の日付や50分後の時刻などを簡単に計算して取得できる。**
https://note.nkmk.me/python-datetime-usage/

```python
datetime.datetime.now()
## 2022-11-11 04:18:08.496290
## year-month-day hour:minute:second.microsecond
## YYYY-mm-DD HH:MM:SS.ffffff
## %Y-%m-%d %H:%M:%S.%f

timestr = "2022-11-11 04:18:08.496290"
print(datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S.%f"))
```


### ファイルの圧縮率

https://ishitonton.hatenablog.com/entry/2020/09/18/000035

- parquetの時点で非圧縮でも圧縮率は高い