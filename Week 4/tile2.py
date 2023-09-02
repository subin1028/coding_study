num = int(input())
d = [0] * (num + 2)

d[1] = 1
d[2] = 3

for i in range(3, num+1):
    d[i] = (d[i-1] + d[i-2] * 2) % 10007
    
print(d[num])


# d[3] = 5
# d[4] = 11