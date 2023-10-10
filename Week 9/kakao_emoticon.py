from itertools import product
def solution(users, emoticons):
    answer = []
    pay = 0
    discount = [10, 20, 30, 40]
    n = len(emoticons)
    com_dis = list(product(discount, repeat=n))

    for comb in com_dis:
        count = 0
        temp_pay = 0
        for user in users:
            pay = 0
            for k in range(0, len(emoticons)):
                if user[0] <= comb[k]:
                    pay += emoticons[k] // 100 * (100-comb[k]) 
                    
            if pay >= user[1]:
                count += 1
            else:
                temp_pay += pay
                
        answer.append([count, temp_pay])
    answer = sorted(answer, key=lambda x: (x[0], x[1]))
    print(answer[-1])
    return answer[-1]

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]] #비율 이상의 할인이 있는 이모티콘 모두 구매
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)

a = [4, 13860]