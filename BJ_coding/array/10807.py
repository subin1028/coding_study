N = int(input())
nums = list(map(int, input().split()))
fnd = int(input())
ans = 0
for i in nums:
    if fnd == i:
        ans += 1
print(ans)