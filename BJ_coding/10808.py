import sys
alpha = {}
word = list(sys.stdin.readline().strip())
for i in range(97, 123):
    alpha[chr(i)] = 0

for s in word:
    alpha[s] += 1

answer = list(alpha.values())

print(*answer)