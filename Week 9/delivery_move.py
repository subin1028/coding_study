def solution(fee, comp, shippings) :
    answer = 0
    days = [idx for idx, x in enumerate(shippings) if x != 0]
    add = [[] for i in range(len(days)-1)]
    dp = [0 for i in range(len (days) -1)]
    count = lambda x: sum(1 for i in x if i != 0)
    answer = count (shippings) * fee
    
    def add_money(f_idx, s_idx, comp, shippings) :
        return (s_idx - f_idx) * shippings [f_idx] * comp
    
    for i in range(0, len(days) -1):
        for j in range(i+1, len(days)):
            a = add_money (days[i], days[j], comp, shippings)
            add[i].append(a)
    print(add)
    
    for a in add:
        for idx, aa in enumerate(a):
            if aa < fee:
                dp[idx] += aa + (len(days ) -1) * fee
    
    answer = min(x for x in dp if x != 0)
    return answer