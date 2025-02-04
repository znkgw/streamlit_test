#可視化技術課題レポート
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
plt.rcParams['font.family'] = 'Meiryo'

st.title("可視化技術課題レポート")

st.header("1.Matplotlibの使い方")
"""
1.Matplotlib
+ Pythonにおいて最も利用されている可視化ライブラリ
```python
#matplotlib.pyplot モジュールのインポート
import matplotlib.pyplot as plt
#日本語を表示できるように設定
plt.rcParams['font.family']='Meiryo'
```
2.Matplotlibのグラフ構造
+ レイヤー構造になっている。
+ 土台から描画領域（Figure）、グラフエリア（axes）、軸（axis）、軸目盛（tick）

3.グラフの作成
+ pyplotインターフェイス
  - pltに各種グラフのメソッドを繋げてグラフを描く方法
  - 手軽に書くことができるため、探索的データ分析（EDA）など、ちょっとしたデータ確認のために簡単なグラフ作成で事足りる場合には便利な方法
+ オブジェクト指向インターフェース
  - 変数に plt.figure や plt.subplots などグラフオブジェクトを代入し、そのオブジェクトに対して設定を記入する方法
  - 複雑なグラフや微調整が必要な場合に利用される

```python
## pyplot インターフェース
plt.plot(データ)
plt.show()
## オブジェクト指向インターフェース
#描画領域を作成
fig = plt.figure()
#グラフエリアを作成
ax1 = fig.add_subplot(縦軸, 横軸, 場所)
#複数のグラフエリアの作成
ax2=fig.add_subplot(縦軸, 横軸, 場所)
ax3=fig.add_subplot(縦軸, 横軸, 場所)
ax4=fig.add_subplot(縦軸, 横軸, 場所)
#作成したグラフエリアにプロット
ax1.plot(データ)
ax2.plot(データ)
ax3.plot(データ)
ax4.plot(データ)
plt.show()
```
"""
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
st.pyplot(fig)

st.header("2.折れ線グラフの描画 ")
"""
1.折れ線グラフ
+ データの時間的な変化を表すために利用するグラフ表現
+ 基本x 軸に時間を、y 軸に着目する要素の値を取る
⁺ matplotlib では、.plot()メソッドを用いて表現する。

2.折れ線グラフのオプション引数
+ plot()に指定できるオプション引数
"""
image = Image.open('図１.jpeg')
st.image(image, use_column_width=True)
"""
+ 色や、マーカーの指定方法
"""
image = Image.open('表2.jpeg')
st.image(image, use_column_width=True)
"""
+ 使用例

```python
#線種の指定
plt.plot(データ, linestyle='--')
#マーカーの形と色、複数のオプションの設定
plt.plot(データ, marker='o', color='red')
#線の幅の設定
plt.plot(データ, linewidth=3)

```
+ 凡夫の設定を行う.legend()のオプション引数
  - 凡夫の設定を行うにはラベルを追加する必要がある
"""
image = Image.open('表3.jpeg')
st.image(image, use_column_width=True)
"""
+使用例
```python
plt.plot(データ, label=ラベル名) # ラベル設定を追加
plt.plot(データ, label=ラベル名)
plt.plot(データ, label=ラベル名)
plt.plot(データ, label=ラベル名)
plt.legend(loc='upper right', shadow=True) # 凡例の描画設定
plt.show()
```

+ 軸や目盛の設定を行うメゾット
"""
image = Image.open('表4.jpeg')
st.image(image, use_column_width=True)

"""
+使用例
```python
plt.plot(データ, label=ラベル名)
plt.plot(データ, label=ラベル名)
plt.plot(データ, label=ラベル名)
plt.plot(データ, label=ラベル名)
plt.xlabel('2022 年 8 月') # x 軸ラベル
plt.ylabel('気温（℃）') # y 軸ラベル
plt.grid() # グリッド線の追加
plt.show()
```
+ 時系列目盛の作成
   - 時系列データを表すカラムをdatatime型にする。
   - plt.gcf().autofmt_xdate():列が重ならないように文字を回転して表示する

+ 面グラフの作画
  - カテゴリーが 2 種類以上あるとき、値を積み上げて描画することで、カテゴリー全体の時間的な変化と各カテゴリーの時間的な変化の二つの情報を一度に表現できる
  - .stackplot()を用いて作画する
  - .legend(loc=)で広がり方を設定できる。負の方向:’weighted_wiggle,’上下対照:’sym’

+使用例
```python
plt.stackplot(x軸データ, y軸データ, y2軸データ, y3軸データ, labels=labels)
plt.legend(loc='upper left')#広がり方の設定ができる。
plt.show()
```
"""

