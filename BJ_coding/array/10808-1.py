def func2(arr, N):
    num = [0] * 101
    for i in arr:
        if num[100-i] == 1:
            return 1
        num[i] = 1
    return 0

print(func2([4,13,63,87], 4))