t_num = int(input())
wine = []

for i in range(t_num):
    num = int(input())
    wine.append(num)
    
d = [0] * (t_num)
d[0] = wine[0]
if t_num > 1:
    d[1] = wine[0] + wine[1]

if t_num > 2:
    d[2] = max(wine[0]+wine[2], wine[1]+wine[2], d[1])

for i in range(3, t_num):
    d[i] = max(d[i-1], d[i-3]+wine[i-1]+wine[i], d[i-2]+wine[i])
    
print(d[-1])
