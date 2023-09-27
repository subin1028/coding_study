from collections import Counter
n1 = int(input())
a = list(map(int, input().split(" ")))
n2 = int(input())
b = list(map(int, input().split(" ")))
answer = []

a_count = Counter(a)
for i in b:
    answer.append(a_count[i])

answer = ' '.join(map(str, answer))
print(answer)