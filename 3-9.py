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
result = ''
for i, s in enumerate(lst):
    if i > 0:
        result += '@'
    result += s
print(result)

# クイズの答え：3（foo@bar@baz@@）
