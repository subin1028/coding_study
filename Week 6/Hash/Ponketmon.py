def solution(nums):
    answer = 0
    ans = set(nums) #nums의 최소 요소만 가지기
    if len(ans) >= len(nums) // 2: #만약 nums의 길이 / 2보다 크거나 같으면
        answer = len(nums) // 2 # 최대 nums길이 / 2만큼 포켓몬 get 가능!
        
    elif len(ans) < len(nums) // 2: #더 적으면
        answer = len(ans) #ans길이 만큼만 가져갈 수 있음
    return answer