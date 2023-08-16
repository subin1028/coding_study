from collections import deque
global count #네트워크 개수를 담을 변수
count = 0

def solution(n, computers):
    global count
    answer = 0
    visited = [False] * (n+1) #방문 체크 리스트 생성
    graph = [[] for _ in range(n+1)] #그래프 생성
    for i in range(1, n+1):
        pos = [p+1 for p in range(n) if computers[i-1][p]==1] #방문 위치 정리 / [0,1,1]일 경우 [2,3] 반환
        graph[i] += [v for v in pos if i != v] #자기 위치를 제외한 나머지 위치 저장
        
    for i in range(1, n+1):
        bfs(graph, i, visited)
        
    answer = count
    return answer

def bfs(graph, start, visited):
    global count
    queue = deque()
    if visited[start] == False:
        visited[start] = True
        queue.append(start)
    
        while queue:
            v = queue.popleft()
            
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                     
        count += 1
    return 0