import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Meiryo'
import sweetviz as sv

st.title("ダイヤモンドの品質と価格データの探査的データ分析")

st.header("1.ダイヤモンドの評価に対する基本事項")
"""
1.評価の4C
  + carat  : ダイヤモンドの重さ、数字が大きい方が高評価
  + cut    : ダイヤモンドの輝き、idealが最高評価でPremium、Very Good、good、fairの順
  + color  : ダイヤモンドの色、色コードで示し無色の方が高評価
  + clarity: ダイヤモンドの透明度、状態をコードで示し不純物が無く透明度の高い者の方が高評価

2.ダイヤモンドの形: depth
  + depthはダイヤモンドの形のバランスを表す指標の1つ。単位はパーセントで、59%～62%の範囲が最適

3.ダイヤモンドの形: table
  + tableはダイヤモンドを上から見たときに見える面の大きさを表す指標の1つ。単位はパーセントで、58%前後が最適とされる

4. price
  + 1カラットあたりの価格、状態によって1500ドル～20000ドルと幅がある

5. x、y、z
  + ダイヤモンドのサイズを測ったもの
"""
st.header("2.データの確認")
df=pd.read_csv("./data/diamonds.csv",encoding="utf-8")

"""
本分析は、「diamonds.csv」ファイルを対象に探索的データ分析を行った。まずは、この
CSV ファイルの基本情報を概観する。まずは次のコードでデータを読み込み、データ数と欠
損値の確認を行った。

```python
#データの読み込みと中身の確認
df=pd.read_csv("./data/diamonds.csv",encoding="utf-8")
#データフレームのサイズ
df.shape
#欠損値の確認
df.isnull().sum()
```
"""
st.text(f"この結果、データサイズは{df.shape}であり、欠損値はなかった。")
st.write(df.isnull().sum)

"""
次に、データフレームの概要と基本的統計量を示す。実行コードはそれぞれ次のとおりである。

```python
# 概要表示
df.head()
#基本統計量の算出
df.describe().round(2)
```
"""

