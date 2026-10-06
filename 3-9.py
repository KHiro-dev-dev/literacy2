################### 
# 第３回_3-9
####################

'''
⽂字列のメソッドjoinを使って，リスト['foo', 'bar', 'baz', '@']を「@」を挟んで結合すること．同
じことを，joinを使わずにループで実現すること．
クイズ：結果は？

1. foo@bar@baz
2. foo@bar@baz@
3. foo@bar@baz@@
4. foo@bar@baz@@@
'''
# [ クイズ1 ]
lst = ['foo', 'bar', 'baz', '@']

# joinを使う方法
print('@'.join(lst))

# joinを使わずにループで実現する方法
# 結果を入れる空の文字列を用意する
result = ''
# enumerateを使うと、要素(s)と一緒に番号(i)も取り出せる
# i=0:'foo', i=1:'bar', i=2:'baz', i=3:'@'
for i, s in enumerate(lst):
    # 先頭の要素(i=0)の前には区切りを入れない
    # 2番目以降は、要素を足す前に区切りの'@'を足す
    if i > 0:
        result += '@'
    # 要素そのものを後ろにつなげる
    result += s
# 途中経過:
#   i=0: 'foo'
#   i=1: 'foo' + '@' + 'bar'         -> 'foo@bar'
#   i=2: 'foo@bar' + '@' + 'baz'     -> 'foo@bar@baz'
#   i=3: 'foo@bar@baz' + '@' + '@'   -> 'foo@bar@baz@@'
print(result)

# クイズの答え：3（foo@bar@baz@@）
