from bisect import bisect_left, bisect_right
n1 = int(input())
a = list(map(int, input().split(" ")))
n2 = int(input())
b = list(map(int, input().split(" ")))
answer = [0 * i for i in range(n2)]
b_copy = []

a.sort()

for i, j in enumerate(b):
    b_copy.append([j, i])

b_copy.sort()

for num, idx in b_copy:
    if bisect_left(a, num) > len(a)-1:
        continue
    else:
        if num == a[bisect_left(a, num)]:
            answer[idx] = 1
        else:
            continue

for j in answer:
    print(j)

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5