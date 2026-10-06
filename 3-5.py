################### 
# 第３回_3-5
####################

'''
濁点付きの平仮名の「か」は，「が」（U+304C），または，「か」＋濁点（U+3099）で表現できる．
しかし，そのままでは'が'と'が'は同じとはみなされない．ユニコード正規化について説明してから，
「が」（U+304C）と「か」＋濁点（U+3099）を同じとみなす方法を説明すること．
クイズ：ユニコード正規化で，U+795EとU+FA19は

1. 同じになる
2. 同じにならない
'''
# [ クイズ1 ]
import unicodedata

s1 = 'が'
s2 = 'が'
print(s1, s2)
print(s1 == s2)  # False

# ユニコード正規化：見た目が同じ文字列を、決まった形に揃えるしくみ。
# NFCは「合成」した形（が）に、NFDは「分解」した形（か＋濁点）に揃える。
n1 = unicodedata.normalize('NFC', s1)
n2 = unicodedata.normalize('NFC', s2)
print(n1 == n2)  # True

# クイズ：U+795EとU+FA19
a = '神'
b = '神'
print(a == b)
print(unicodedata.normalize('NFC', a) == unicodedata.normalize('NFC', b))
# 答え：1（互換漢字は正規化で同じになる）
