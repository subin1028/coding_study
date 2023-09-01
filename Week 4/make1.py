num = int(input())
count = 0
while(num != 1):
    if num % 3 == 0:
        num /= 3
        count += 1
        
    elif num % 2 == 0:
        num /=2
        count += 1
        
    else:
        num -= 1
        
print(count)