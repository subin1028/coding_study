def solution(people, limit):
    answer = 0
    people.sort()
    
    min = 0
    max = len(people) - 1
    print(people)
    while min < max:
        print(people[min] + people[max])
        if people[min] + people[max] <= limit:
            answer += 1
            min += 1
        max -= 1

    return len(people) - answer

people = [70, 50, 80, 50]
limit = 100

solution(people, limit)