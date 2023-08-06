import matplotlib.pyplot as plt
#plt.style.use('seaborn-darkgrid') 古いバージョンしか対応していないくえらーがでるため、処理を殺しています。

x = np.linspace(0, 2, 3) #勤務日数　プロット数を定義
y1 = [8,8,0] #直近3日間の勤務時間
y2 = [0,1.8,3.7]#直近3日間の勉強時間
 
# 左上
plt.subplot(1,2,1) #subplot(行数, 列数, プロット番号)
ax1 = plt.subplot(1,2,1)
ax1.set_title("柴山の勤務時間", color="black",fontname='MS Gothic')
plt.plot(x, y1, label='time(h)')
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f')) #軸の桁表示を設定
plt.legend(loc=(0.1,0.1))
 
# 右上
plt.subplot(1,2,2)

ax2 = plt.subplot(1,2,2)
ax2.set_title("柴山の勉強時間", color="black",fontname='MS Gothic')
plt.plot(x, y2, label='time(h)')
plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
plt.legend()

plt.show()