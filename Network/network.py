def count_tower(n, num, wires, select):
    oth_num = []
    cnt_num = 1
    
    for i in wires:
        if i != select:
            if num in i:
                cnt_num += 1
                oth_num += [oth for oth in i if (num in i)&(oth!=num)]
            
    for i in wires:
        if i != select:            
            for j in oth_num:
                if (j in i) and ((num in i) == False):
                    cnt_num += 1

    cha = abs((n - cnt_num) - (cnt_num))
    return cha   
    

def solution(n, wires):
    count = []
    
    for i in wires:
        select = i
        num = i[0]
        ans = count_tower(n, num, wires, select)
        count.append(ans)
    
    answer = min(count)
    return answer
