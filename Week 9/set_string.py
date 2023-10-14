dic, check = list(map(int,input().split(" ")))
dic1 = []
check1 = ""
sum = 0

for i in range(dic):
    dic1.append(input())
    
for i in range(check):
    check1 = input()
    if check1 in dic1:
        sum += 1

print(sum)