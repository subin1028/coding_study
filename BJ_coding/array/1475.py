nums = [0] * 10
ans = 0
room = list(map(int, input()))

for i in room:
    nums[i] += 1

ans = max(max([x for i, x in enumerate(nums) if i != 6 and i != 9]), (nums[6] + nums[9] + 1) // 2)
print(ans)