
def solution(numbers, target):
    answer = 0
    result = [0]
    for i in numbers:
        temp = []
        for j in result:
            temp.append(j + i)
            temp.append(j - i)
        
        result = temp
            
    for num in result:
        if num == target:
            answer += 1

    return answer