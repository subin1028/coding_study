N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N):
    t, p = info[i]
    money = 0
    if (i+t) < N:
        if dp[i] != 0:
            dp[i+t] = max(dp[i+t], dp[i] + p)

        else:
            if i > 1:
                dp[i+t] = max(dp[i+t], p, sum(dp[:i-1])+p)

print(dp)
