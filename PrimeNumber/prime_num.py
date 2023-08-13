def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    
    return answer