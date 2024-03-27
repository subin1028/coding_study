from collections import Counter
num = 1
for _ in range(3):
    num *= int(input())

ans = Counter(str(num))

for i in range(10):
    print(ans[str(i)])