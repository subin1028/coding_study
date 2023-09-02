f_num = int(input())
number = []
for i in range(f_num):
    num = int(input())
    number.append(num)
    
d = [0] * (max(number)+2)

d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, max(number)+1):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for j in number:
    print(d[j])

# d[4] = 7
# d[5] = 13
# d[6] = 24
# d[7] = 44