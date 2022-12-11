import io
import gzip
import csv
import os
import pandas as pd

# step1 make a gzip
df = pd.DataFrame({
    'name' :['rinze', 'natsuha', 'cyoko'],
    'actor' : ['maruoka', 'akiho', 'harusu'],
    'height' : [178, 173, 169]
})
print(df)
df.to_csv("foo.test.csv.gz", compression="gzip", index=False)

print("writing data to gzipped file.")

# step2 read gzip
# https://qiita.com/shotakaha/items/c11c5d9c6e0788dc4bdf
print("read gzip")
df2 = pd.read_csv('foo.test.csv.gz', sep='\t', header=0)
print(df2)

# step3 write parquet
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_parquet.html
df2.to_parquet("foo.parquet")
df2.to_parquet("foo.gz.parquet", compression="gzip")
df2.to_parquet("foo.snappy.parquet", compression="snappy")
# 無圧縮
df2.to_parquet("foo.n.parquet", compression=None)

# step4 read parquet
print("read parquet")
df3 = pd.read_parquet("foo.parquet")
print(df3)

print("comp none parquet")
df4 = pd.read_parquet("foo.n.parquet")
print(df4)