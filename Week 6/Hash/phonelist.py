def solution(phone_book):
    answer = True

    if len(phone_book) == 1:
        return True
    
    phone_book.sort()
    
    for i in range(0, len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]: 
                return False               
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)