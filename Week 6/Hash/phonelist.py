def solution(phone_book):
    answer = True
    end = []
    start = []
    
    if len(phone_book) == 1:
        return answer
    
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            start = phone_book[j]
            orin = phone_book[i]
            if len(orin) <= len(start):
                if orin == start[:len(orin)]:
                    return False
    
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)