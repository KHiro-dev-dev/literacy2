################### 
# 第３回_3-10
####################

'''
整数のリストを引数として受けとり，3の倍数を全て-1にした新しいリストを返す関数fを2通りの方法で実装すること．
例えば，f([3, 1, 5])の結果は[-1, 1, 5]である．
1. forとenumerateを使う．
2. forを使い，enumerateを使わない．
クイズ：f([0, 1, 2, 3])の結果は

1. [-1, 1, 2, -1]
2. [-1, 1, 2, 3]
3. [0, 1, 2, -1]
4. [0, 1, 2, 3]
'''
# [ クイズ1 ]
# 1. forとenumerateを使う方法
def f1(lst):
    result = lst.copy()  # 元のリストは変えず、新しいリストを返す
    for i, x in enumerate(result):
        if x % 3 == 0:
            result[i] = -1
    return result

# 2. forを使い、enumerateを使わない方法
def f2(lst):
    result = []
    for x in lst:
        if x % 3 == 0:
            result.append(-1)
        else:
            result.append(x)
    return result

print(f1([3, 1, 5]), f2([3, 1, 5]))
print(f1([0, 1, 2, 3]), f2([0, 1, 2, 3]))
# 答え：1（0も3の倍数なので-1になる）
