
wheel = [] #바퀴 정보
for _ in range(4):
    wheel.append(list(input()))

time = int(input())
times = [] #돌리는 톱니, 방향
for _ in range(time):
    times.append(list(map(int, (input().split(" ")))))
    
info = [] #12시 방향, 오, 왼 톱니
    
for i in wheel:
    info.append([i[0], i[2], i[6]])
    
for num, direct in times:
    a = wheel[num-1][6]     
    
def move(num, num1, dir):
    #num: 돌아가는 톱니, num1: 영향받는 톱니
    if num > num1:
        if info[num-1][2] == info[num1-1][1]:
            circle(num1, dir)
            info[num-1] = [wheel[num-1][0], wheel[num-1][2], wheel[num-1][6]]
                
    if num1 > num: 
        if info[num1-1][2] == info[num-1][1]:
            circle(num1, dir)
            
        
def circle(num, dir):
    if dir == 1:
        for i in range(0, 8):
            wheel[num-1][i] = wheel[num-1][i-1]
        
    elif dir == -1:
        temp = wheel[num-1][0]
        for i in range(0, 7):
            wheel[num-1][i] = wheel[num-1][i+1]
        wheel[num-1][-1] = temp
        
    
# 10101111
# 01111101
# 11001110
# 00000010
# 2
# 3 -1
# 1 1

# 6번째


print(wheel)
print(times)

# [['1', '0', '1', '0', '1', '1', '1', '1']]
# [[3, -1], [1, 1]]