################### 
# 第３回_3-7
####################

'''
メソッドupperで大文字になるのは，ASCIIの小文字のアルファベットだけではない．
メソッドupperで変更される文字を列挙すること．ヒント：ユニコードスカラ値の最大値はsys.maxunicodeである．
クイズ：何文字あるか？

1. 100未満
2. 100以上200未満
3. 200以上1000未満
4. 1000以上
'''
# [ クイズ1 ]
import sys

s = 'ⓐ'
print(s, s.upper())

changed = []
# 0からsys.maxunicodeまで、全部の文字を調べる
for i in range(sys.maxunicode + 1):
    c = chr(i)
    # upperしても変わらない文字は除く
    if c.upper() != c:
        changed.append(c)
print(''.join(changed))
print(len(changed))
# 答え：4（1552文字あるので1000以上）
