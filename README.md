# literacy2
情報リテラシーに使うリポジトリ

```python:
for i in range(len(lst)): # 0,1,2,3,..,i,...len(lst)-1
        for j in range(0,i): #0,1,2,3,..i-1
            if (lst[j] == lst[i]):
                break
        else:
            result.append(lst[i])
    return result
```