def solution(m, n, puddles):
    answer = 0
    graph = [[1] * m for _ in range(n)]
    
    for i in puddles:
        graph[i[0]][i[1]] = 0
 
 
    
    return answer


m = 4
n = 3
puddles = [[1,1]]

solution(m, n, puddles)