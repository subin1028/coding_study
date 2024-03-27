nums = [1] * 10
sets = 1
room = list(map(int, input()))

for n in room:
    if nums[n] > 0: 
        nums[n] -= 1

    elif n == 9 and nums[6] > 0:
        nums[6] -= 1

    elif n == 6 and nums[9] > 0:
        nums[9] -= 1

    else:
        sets += 1
        nums = [x+1 for x in nums]
        nums[n] = 0

print(sets)