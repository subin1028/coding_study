def dfs(x, y):
    global count
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if maps[x][y] == 1:
        count += 1
        maps[x][y] = 0
        
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = m = int(input())
maps = [[] for _ in range(n)]
result = []
for i in range(0, n):
    a = input()
    for num in a:
        maps[i].append(int(num))

count = 0
for k in range(n):
    for j in range(m):
        if dfs(k, j):
            result.append(count)
            count = 0

print(len(result))
result.sort()
for i in result:
    print(i)