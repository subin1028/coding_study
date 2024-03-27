def func2(arr, N):
    for i in arr:
        arr2 = arr.copy()
        arr2.remove(i)
        if 100-i in arr2:
            return 1
        
    return 0


print(func2([4,13,63,87], 4))
