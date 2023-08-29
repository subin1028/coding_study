import copy
def solution(triangle):
    graph = copy.deepcopy(triangle)
    maxi = triangle[0][0]
  
    for i in range(0, len(triangle)-1):
        for j in range(0, len(triangle[i])):
            n = graph[i][j] + triangle[i+1][j]
            m = graph[i][j] + triangle[i+1][j+1]
            if n > graph[i+1][j]:
                graph[i+1][j] = n
                maxi = n
                
            graph[i+1][j+1] = m
            
    answer = max(graph[-1])
    return answer

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

solution(triangle)
