from collections import deque

def mapping(tickets): #항공권을 숫자로 매핑하는 함수
    ticket_dict = {}
    orient = list(set(sum(tickets, []))) #요소 추출
    orient.sort() #알파벳순으로 오도록 정렬
    for i, ticket in enumerate(orient):
        ticket_dict[ticket] = i #딕셔너리 생성
        
    mapp = [[ticket_dict[start], ticket_dict[des]] for start, des in tickets]
    #항공권을 숫자로 매핑
    
    return mapp, len(orient), ticket_dict

def dfs(graph, current, len_tickets, visited, path):
    path.append(current)
    
    if len(path) == len_tickets + 1:
        return True
    
    for next_city in graph[current]:
        if not visited[current][next_city]:
            visited[current][next_city] = True
            if dfs(graph, next_city, len_tickets, visited, path):
                return True
            visited[current][next_city] = False #백트래킹을 위해 제자리
    
    path.pop()
    return False

def solution(tickets):
    answer = []
    mapp, n, ticket_dict = mapping(tickets)
    graph = [[] for _ in range(n)]
    
    for i,j in mapp:
        graph[i].append(j) #그래프 생성
    
    for i in graph:
        i.sort()
    
    visited = [[False] * n for _ in range(n)]
    start_city = ticket_dict["ICN"]
    path = []
    
    dfs(graph, start_city, len(tickets), visited, path)
    
    answer = [list(ticket_dict.keys())[list(ticket_dict.values()).index(city)] for city in path]
    
    
    return answer


tickets = [["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]]
solution(tickets)