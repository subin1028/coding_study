from itertools import product
def solution(word):
    ex = ['A', 'E', 'I', 'O', 'U']
    w_dict = []
    
    for i in range(1, 6):
        for j in product(ex, repeat = i):
            w_dict.append(''.join(j))
            
    w_dict.sort()
    answer = w_dict.index(word) + 1

    print(answer)
    answer = 0
    return answer