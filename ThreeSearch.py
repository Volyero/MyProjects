#!/usr/bin/python3
#
# 2021-11-11
# A.Karim
#
# 3の倍数、１の位が３、１０の位が３の数チェック
#

# メッセージ表示
print("1~50までの整数のうち３の関連数を調べる")
print("該当数 = ", end="")
   
    # 3の位数をカウントする変数cntの初期化
cnt = 0
    
    # 1~50までの整数をチェックする
for i in range(1, 51):
    if i % 3 == 0:     # 3の位数チェック
        cnt += 1
        print(i, end=" ")
    elif i % 10 == 3: # 1の位が３かチェック
        cnt += 1
        print(i, end=" ")
    elif i // 10 == 3: #　１０のくらいが３かチェック
        cnt += 1
        print(i, end=" ")
                  
# 改行
print()
print("count = ", cnt)