import numpy

def make_check(answers, asw):
    share = len(answers) // len(asw)
    remain = len(answers) % len(asw)
    check = list(asw) * int(share)
    check += list(asw[i] for i in range(0, remain))
    return check

def solution(answers):
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    win = [0,0,0]
    
    ch1 = make_check(answers, p1)
    ch2 = make_check(answers, p2)
    ch3 = make_check(answers, p3)
    
    for i in range(0, len(answers)):
        if ch1[i] == answers[i]:
            win[0] += 1
            
        if ch2[i] == answers[i]:
            win[1] += 1
            
        if ch3[i] == answers[i]:
            win[2] += 1
            
    winner = max(win)
    answer = list(x+1 for x in filter(lambda x: win[x] == winner, range(len(win))))
    print(answer)
    return answer

answers = [1,2,3,4,5,1,2,3,4,5,6,8,9,4,5,6,5]
asw = [1,2,3,4,5]
solution(answers)