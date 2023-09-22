def solution(phone_book):
    answer = True
    end = []
    start = []
    
    if len(phone_book) == 1:
        return True
    
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            temp = phone_book[j].replace(phone_book[i], "a")
            if temp[0] == "a":
                print("false")
                return False
    print("true") 
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)