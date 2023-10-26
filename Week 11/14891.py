
wheel = [] #바퀴 정보
for _ in range(4):
    wheel.append(list(input()))

time = int(input())
times = [] #돌리는 톱니, 방향
for _ in range(time):
    times.append(list(map(int, (input().split(" ")))))
  
def circle(num, dir):
    if dir == 1:
        for i in range(0, 8):
            wheel[num-1][i] = wheel[num-1][i-1]
        
    elif dir == -1:
        temp = wheel[num-1][0]
        for i in range(0, 7):
            wheel[num-1][i] = wheel[num-1][i+1]
        wheel[num-1][-1] = temp
  
def left(num, dir):
    if num < 1:
        return
    if wheel[num][2] != wheel[num+1][6]:
        left(num-1, -dir)
        circle(num, dir)
        
def right(num, dir):
    if num > 3:
        return
    if wheel[num][6] != wheel[num-1][2]:
        right(num+1, -dir)
        circle(num, dir)
    
for num, direct in times:
    left(num-1, -direct)
    right(num+1, -direct)   
    circle(num, dir)
    
score = 0
if wheel[0][0] == '1':
    score += 1
for i in range(1, 4):
    if wheel[i][0] == '1':
        score += i * 2

print(score)

# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1

# [['1', '0', '1', '0', '1', '1', '1', '1']]
# [[3, -1], [1, 1]]
