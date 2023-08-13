from itertools import permutations
def check_prime(num):
    if num <= 1:
        return 0
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    li_num = list(numbers)
    permu_list = list(permutations(li_num, 1))
    permu_list += list(permutations(li_num))
    f_nums = [int(''.join(num)) for num in permu_list]
    
    for i in f_nums:
        if(check_prime(i)):
            answer += 1
   
    return answer