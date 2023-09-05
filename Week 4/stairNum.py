num = int(input())

d = [0] * (num+2)
d[1] = 9

for i in range(2, num+1):
    d[i] = (d[i-1] * 2 - (i-1)) % 1000000000
    
print(d[num])