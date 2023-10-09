def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    land = [x[0:2] for x in costs]
    land = set(tuple(x) for x in land)
    print(land)
    return answer

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
solution(n, costs)