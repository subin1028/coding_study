def solution(name):
    answer = 0
    name = list(name)
    n = len(name)-1
    for i, j in enumerate(name):
        if j != "A":
            answer += min(ord(j) - ord("A"), (ord("Z") - ord(j))+1)
        
        j = i + 1
        while j < len(name) and name[j] == 'A':
            j += 1
            
        min_n = min(min_n, i + i + len(name) - j)
                    
        if i < n:
            k = i + 1
            n = min(n, i + len(name) - j + min(i, len(name) - j))
            
        
    
    
    answer += n  # 커서 이동 횟수 더하기
    answer
    return answer


name = "JAZ"
solution(name)