def solution(name):
    # ord: 문자를 유니코드(정수)로 변환해주는 함수
    # 로직을 2가지로 나눔
    # 1번째 로직: 왼쪽으로 갈지, 오른쪽으로 갈지 정하기
    # 2번째 로직: 위로 갈지, 아래로 갈지
    alpha = [min(ord(i)-ord('A'), ord('Z')-ord(i)+1) for i in name]
    idx, answer = 0, 0
    
    while True:
        answer += alpha[idx]
        alpha[idx] = 0 # 이동을 하면, 그 값은 0으로 바꿔줌
        
        if sum(alpha) == 0:
            return answer
        
        left, right = 1, 1 # 왼쪽, 오른쪽으로 움직일 때 이동하는 거리
        # 글자가 나올 때까지 while문
        while alpha[idx - left] == 0: 
            left += 1
        while alpha[idx + right] == 0:
            right += 1
        
        # 최소거리 구하기
        if right > left:
            answer += left
            idx -= left
        else:
            answer += right
            idx += right
            
    print(answer)
            
solution("ABABAABA")