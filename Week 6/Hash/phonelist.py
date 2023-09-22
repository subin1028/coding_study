def solution(phone_book):
    answer = True

    if len(phone_book) == 1: #1글자면 바로 True 반환
        return True
    
    phone_book.sort() #같은 시작값끼리 최대한 붙도록 정렬
    
    for i in range(0, len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]): #접두사 비교할 숫자 길이가 더 길면
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]: #접두사인지 비교
                return False  #False 반환             
    return answer

phone_book = ["12", "123", "1235", "567", "88"]
solution(phone_book)