from itertools import combinations
def solutions(cards):
    answer = 0
    card = {}
    ws = list(set(cards))
    joke = 0
    
    def reset():
        for i in ws:
            if i != 0:
                card[i] = 0
            
    reset()
    for i in cards:
        if i == 0:
            joke += 1
            
        else:
            card[i] += 1
        
        values = list(card.values())
        if(sum(values) + joke >= 5):
            com_values = [[0,0]]
            com_values += list(combinations(values, 2))
            for v in com_values:
                if 2 in v and 3 in v:
                    answer += 1
                    reset()
                    joke = 0
                    break
                    
                elif sum(v) + joke == 5:
                    answer += 1
                    reset()
                    joke = 0
                    break
     
    print(answer)            
    return answer

cards = [0,0,0,0,0]
solutions(cards)