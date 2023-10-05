n,t = list(map(int, input().split(' ')))

array = [int(input()) for _ in range(n)]

start = 1
end = max(array)

while(start <= end):
    total = 0
    mid = (start + end) // 2
    for i in array:
        if i >= mid:
            total += i//mid
            
    if total < t:
        end = mid - 1
        
    else:
        start = mid + 1
        
print(end)