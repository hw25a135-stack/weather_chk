import pandas as pd
import matplotlib.pyplot as plt

# CSVを読み込む（5行スキップ）
df = pd.read_csv('data.csv', skiprows=5, encoding='shift_jis')

# 列の名前を強制的にシンプルな名前に付け替える
df.columns = ['年月日', '平均気温', '品質情報', '均質番号']

# グラフを描画する
plt.plot(df['年月日'], df['平均気温'])
plt.title('Temperature' , fontsize=16)
plt.xlabel('Date')
plt.ylabel('Temperature (C)')

#書き込みその１
# グラフを画面に表示
plt.show()
