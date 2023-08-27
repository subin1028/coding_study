def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    if check[x][y] == 0:
        check[x][y] = 1
        
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n = m = int(input())
answer = 0

def calcul():
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                result += 1
    if answer < result:
        answer = result

graph = []
max_num = 0
for i in range(n):
    graph.append(list(map(int, input().split(" "))))
    if max(graph[-1]) > max_num:
        max_num = max(graph[-1])

check = []
for i in range(1, max_num+1):
    check = [[num < i for num in row] for row in graph]
    calcul()

print(answer)