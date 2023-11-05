N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

length = []
length.append(lines[0][0])
length.append(lines[0][1])

for i in range(1, N): #lines
    for j in range(1, len(length), 2): #length
        if lines[i][0] <= length[j]:
            del length[j]
            length.append(lines[i][1])
            
        else:
            length.append(lines[i][0])
            length.append(lines[i][1])
            
result = sum(length[i] - length[i-1] for i in range(1, len(length),2))
print(result)
        

#첫번째 점과 마지막 점을 넣는다
#다음 조합의 첫번째 점과 마지막 점을 비교한다
#다음 첫번째가 이전 마지막보다 작거나 같으면
#마지막 점을 제거하고 다음의 마지막 점을 넣는다
#만약 else면
#그 점의 첫번째와 마지막을 넣는다

# 4
# 1 3
# 2 5
# 3 5
# 6 7