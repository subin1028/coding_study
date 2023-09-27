n1 = int(input())
a = list(map(int, input().split(" ")))
n2 = int(input())
b = list(map(int, input().split(" ")))
answer = []

a.sort()
b.sort()

for i in b:
    st = (n1-1) // 2
    while(1):
        if a[st] == i:
            answer.append(1)
            break
            
        elif a[st] > i:
            try:
                st = st // 2
            except:
                answer.append(0)
                break
        
        elif a[st] < i:
            try:
                st = (st + (n1-1)) // 2
            except:
                answer.append(0)
                break
    
print(answer)

# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5