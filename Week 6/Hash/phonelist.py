def solution(phone_book):
    answer = True
    end = []
    start = []
    
    if len(phone_book) == 1:
        return True
    
    for i in phone_book:
        for j in phone_book:
            if i == j: continue
            else:
                if j[0] == i[0]:
                    temp = i.replace(j, "a")
                    temp1 = j.replace(i, "a")
                    if temp[0] == "a" or temp1[0] == "a":
                        return False
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)