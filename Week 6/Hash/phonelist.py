def solution(phone_book):
    answer = True

    if len(phone_book) == 1:
        return True
    
    phone_book.sort()
    
    #한 번 true인 애들이 또 검사된다
    for i in range(0, len(phone_book)-1):
        for j in range(i+1, len(phone_book)):
            if phone_book[i][0] != phone_book[j][0]:
                    break
            else:
                temp = phone_book[i].replace(phone_book[j], "a")
                temp1 = phone_book[j].replace(phone_book[i], "a")
                if temp[0] == "a" or temp1[0] == "a":
                    return False               
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)