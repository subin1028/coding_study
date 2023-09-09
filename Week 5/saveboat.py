def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    
    while len(people) > 0:
        min = people.pop()
        if not people:
                answer += 1
                break
            
        for i in range(len(people), -1, -1):
            if(min + people[-1] <= limit):
                people.pop()
                answer += 1
            
        else:
            answer += 1
            
    print(answer)
    return answer

people = [20, 20, 40, 50, 30, 60]
limit = 100

solution(people, limit)