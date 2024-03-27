alpha = [0]*26
word = list(input())

for s in word:
    alpha[ord(s)-97] += 1

print(*alpha)