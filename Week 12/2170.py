N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

s, e = lines[0]
length = e - s

del lines[0]

for start, end in lines:
    if start <= e and end > e: #다음 첫번째가 이전 마지막보다 작거나 같으면
            length += (end - e)
            e = end
        
    elif start > e:
        length += (end - start)
        e = end
        
print(length)
        
#다음 첫번째가 이전 첫번째보다 작다면?
#첫번째 점과 마지막 점을 넣는다
#다음 조합의 첫번째 점과 마지막 점을 비교한다

#마지막 점을 제거하고 다음의 마지막 점을 넣는다
#만약 else면
#그 점의 첫번째와 마지막을 넣는다

# 4
# 1 3
# 2 5
# 3 5
# 6 7