n = int(input())
nums = list(map(int, input().split()))
x = int(input())
ans = 0
check = [0] * 1000001

for i in nums:
    if x-i <= 1000000 and check[x-i] == 1:
        ans += 1
    check[i] = 1

print(ans)