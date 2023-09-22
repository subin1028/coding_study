def solution(clothes):
    answer = 1
    cloth = {}
    count = []

    for i,j in clothes: #i는 옷 이름, j는 옷 종류
        if j not in cloth: #만약 딕셔너리에 옷 종류가 없다면
            cloth[j] = [i]   #종류 추가하고 값으로 옷 이름 넣어주기
        else:
            cloth[j].append(i) #있다면 옷 종류에 새로운 옷 이름 추가
            
    for k in cloth.keys(): #딕셔너리의 키만 뽑아서
        count.append(len(cloth[k])) #키에 대한 값의 개수를 리스트로 넣어주기
        
    for h in count:
        answer *= (h+1) #모든 경우의 수 계산
    
    return answer-1 # 아무것도 안 입는 경우 빼주기

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)