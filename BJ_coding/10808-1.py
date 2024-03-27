def func2(arr, N):
    for i in range(N):
        if 100-arr[i] in arr[:i-1]:
            return 1
        
    return 0


print(func2([4,13,63,87], 4))
