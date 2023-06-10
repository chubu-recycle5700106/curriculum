#問題①
#問1-1
# int型のリストdataを作成し、値を1,3,5,7で初期化
list = [1,3,5,7]

i = 0

for i in list:
    print(i*i)

#問1-2
j = 0
for j in range(8):
    if j %2 == 1:
     a = j**2
     print(a)
