cha = [[0 for _ in range(27)] for _ in range(2)]
s1 = input()
s2 = input()
res = 0

for i in s1:
    cha[0][ord(i)-97] += 1

for j in s2:
    cha[1][ord(j)-97] += 1

for s in range(27):
    res += abs(cha[0][s] - cha[1][s])

print(cha)