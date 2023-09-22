def solution(clothes):
    answer = 0
    sum = 0
    num = 0
    cloth = {}
    count = []
    for i,j in clothes:
        num += 1
        if j not in cloth:
            cloth[j] = [num]   
        else:
            cloth[j].append(num)
            
    for k in cloth.keys():
        count.append(len(cloth[k]))
        
    for h in count:
        answer *= (h+1)
    
    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)