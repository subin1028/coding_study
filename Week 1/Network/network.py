from collections import deque
def bfs(graph, v, visited): #방문하는 송전탑 개수 구하기
    queue = deque()
    queue.append(v)
    visited[v] = True #시작점 방문처리
    
    while queue:
        v = queue.popleft()
        print(v, end= ' ')
        
        for i in graph[v]: #트리에서 연결된 지점 찾아서
            if not visited[i]:
                queue.append(i)
                visited[i] = True #방문 처리하기
                
    return visited.count(True) #방문한 곳 개수 리턴

def solution(n, wires):
    count = [] #개수 차가 들어갈 리스트
    for a in wires:
        print(a)
        graph = [[] for _ in range(n+1)] #그래프 크기 조정
        visited = [False] * (n+1) #방문 확인할 그래프
        copy_wire = wires[:] #wires 요소 복사
        copy_wire.remove(a) #제거할 경로 삭제
        
        for i,j in copy_wire:
            graph[i] += [j] #트리 생성
            graph[j] += [i]
        ans = bfs(graph, a[0], visited) 
         #삭제한 경로의 첫번째 값을 시작점으로 방문 개수 구하기
        count.append(abs(n - ans*2)) #방문한 곳 차이 구하기
        
    answer = min(count) #가장 적은 차이 리턴
    return answer