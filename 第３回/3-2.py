################### 
# 第３回_3-2
####################

'''
Pythonの，①文字列のメソッドformatと，②f文字列（f-strings）の使い方を，具体例を使って説明すること．
クイズ：x = 3.1415とする．振る舞いの違うものはどれであるか．

1. print(f'{x = :.3f}')
2. print(f'x = {x:.3f}')
3. print('x = {:.3f}'.format(x))
4. print('x = ' + format(x, '.3f'))
5. 全部同じ
'''
# [ クイズ1 ]
x = 3.1415
name = 'foo'

# ① formatメソッド：文字列中の {} に引数が順に入る。{:.3f} は小数点以下3桁
print('x = {:.3f}'.format(x))
print('{} さんの値は {:.2f}'.format(name, x))
print('{1} {0}'.format('a', 'b'))  # 番号で位置を指定できる

# ② f文字列：先頭にfを付け、{}の中に式を直接書く
print(f'x = {x:.3f}')
print(f'{name} さんの値は {x:.2f}')
print(f'{x + 1:.1f}')  # 式も書ける
print(f'{x = :.3f}')  # {x = } は「x = 値」と表示するデバッグ用の書き方

# クイズの4つを実行して比べる
print(f'{x = :.3f}')
print(f'x = {x:.3f}')
print('x = {:.3f}'.format(x))
print('x = ' + format(x, '.3f'))
# 答え：5（全部 x = 3.142 と表示される）
