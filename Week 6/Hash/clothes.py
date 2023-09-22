def solution(clothes):
    answer = 1
    cloth = {}
    count = []

    for i,j in clothes:
        if j not in cloth:
            cloth[j] = [i]   
        else:
            cloth[j].append(i)
            
    for k in cloth.keys():
        count.append(len(cloth[k]))
        
    for h in count:
        answer *= (h+1)
    
    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)