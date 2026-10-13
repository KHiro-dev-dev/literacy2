################### 
# 第３回_3-8
####################

'''
文字列'foo,bar,baz'をメソッドsplitを使ってコンマで分割すること．
同じことを，splitを使わずにループで実現すること．
クイズ：結果は？

1. ['foo', 'bar', 'baz']
2. ['foo', 'bar,baz']
'''
# [ クイズ1 ]
s = 'foo,bar,baz'

# splitを使う方法
print(s.split(','))

# splitを使わずにループで実現する方法
result = []
current = ''  # いま作っている途中の単語
for c in s:
    if c == ',':
        # コンマが来たら、途中の単語を確定してリストに入れ、次の単語を始める
        result.append(current)
        current = ''
    else:
        current += c
# 最後の単語の後ろにはコンマがないので、ここで入れる
result.append(current)
print(result)
# 答え：1
