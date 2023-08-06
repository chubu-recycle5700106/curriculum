#テキストエディタ
#sample.py

import sys
from keras.datasets import mnist    # ディープラーニングのライブラリの一つ
from PIL import Image    # 画像処理ライブラリ(Pillow)

(X_train, y_train), (X_test, y_test) = mnist.load_data()    # データの読み込み
# (訓練用画像データ, 訓練用ラベル), (テスト用画像データ, テスト用ラベル)

train_no = 0

# 最初の訓練用画像データを表示させる
print('最初の訓練用画像データ(X_train)')
for xs in X_train[train_no]:
    for x in xs:
        sys.stdout.write('%03d ' % x)
    sys.stdout.write('\n')
    
# 最初の訓練用ラベルを表示させる
print('最初の訓練用ラベル(y_train) ＝ %d' % y_train[train_no])
