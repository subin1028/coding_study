from collections import deque

def mapping(tickets): #항공권을 숫자로 매핑하는 함수
    ticket_dict = {}
    orient = list(set(sum(tickets, []))) #요소 추출
    orient.sort() #알파벳순으로 오도록 정렬
    orient.remove("ICN")
    orient.insert(0, "ICN") #ICN이 맨 앞으로 오도록 조정 
    for i, ticket in enumerate(orient):
        ticket_dict[ticket] = i #딕셔너리 생성
        
    mapp = [[ticket_dict[start], ticket_dict[des]] for start, des in tickets]
    #항공권을 숫자로 매핑
    
    print(ticket_dict)
    return mapp, len(orient), ticket_dict

def bfs(graph, start):
    queue = deque()
    ans = []
    
    queue.append(start)
    
    while queue:
        current = queue.popleft()
        print(current, end= ' ')
        ans.append(current)
        
        for i in graph[current]:
            queue.append(i)
            graph[current].remove(i)
            
    return ans
    
def solution(tickets):
    answer = []
    mapp, n, ticket_dict = mapping(tickets)
    graph = [[] for _ in range(n)]
    
    for i,j in mapp:
        graph[i] += [j] #그래프 생성
    
    for i in graph:
        if 0 in i:
            pass
        
        else:
            i.sort()
        
    print(graph)
    pre_ans = bfs(graph, 0)
  
    answer = [code for ans in pre_ans for code, num in ticket_dict.items() if num == ans]
    
    print(answer)
    return answer

tickets = [["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]]

solution(tickets)