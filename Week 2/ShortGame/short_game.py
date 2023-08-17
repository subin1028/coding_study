def solution(maps):
    answer = 0
    n = len(maps) #맵의 세로 길이
    m = len(maps[0]) #맵의 가로 길이

    graph = []
    for i in range(n):
        graph.append(list(map(int, input())))
        
    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1
                
    print(result)
    return answer

def dfs(x,y,graph):
    if x <= -1 or x > = n or y <= -1 or y > = m:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]

solution(maps)
#bfs로 전환