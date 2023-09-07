def solution(n, lost, reserve):
    answer = 0
    have = n - len(lost)
    match = {}
    use_item = []
    
    for i in lost:
        temp = []
        for j in reserve:
            if abs(i - j) == 1:
                temp.append(j)
                match[i] = temp
                
            if i == j:
                break
            
    sorted_match = dict(sorted(match.items(), key=lambda match: len(match[1])))
    
    for i in list(sorted_match.keys()):
        for j in list(sorted_match[i]):
            if j in use_item:
                break
                
            if abs(i - j) == 1:
                have += 1
                del sorted_match[i]
                use_item.append(j)
                break
            
    print(have)
    return have

n = 5
lost = [2, 4]
reserve = [3]

solution(n, lost, reserve)