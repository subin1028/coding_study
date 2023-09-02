num = int(input())

d  = [0] * (num+2)

d[1] = 1
d[2] = 2

for i in range(3, num+1):
    d[i] = (d[i-1] + d[i-2]) % 10007
        
print(d[num])
    
# i = 3) 1, 2 / 3
# i = 4) 2, 3 / 5
# i = 5) 3, 4 / 8