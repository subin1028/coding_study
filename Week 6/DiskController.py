def solution(jobs):
    answer = 0
    t = [] #끝난 시간
    sc = [] #걸린 시간
    jobs.sort()    
    t.append(jobs[0][0] + jobs[0][1])
    sc.append(jobs[0][1])
    
    for i in range(1, len(jobs)):
        wait_time = t[-1] - jobs[i][0]
        if wait_time < 0:
            wait_time = 0 
        sc.append(wait_time + jobs[i][1])
        t.append(sc[-1] + t[-1])
        
    for j in sc:
        answer += j
    answer //= len(jobs)

    print(answer)
    return answer

jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[1,9], [2,6], [0,3]]
solution(jobs)