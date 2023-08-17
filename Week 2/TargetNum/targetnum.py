from itertools import permutations, product
def make_plma(n):
    plma = ['+', '-']
    plma = list(product(plma, repeat = n))
    print(plma)
    return plma

def calculate(plma, nums):
    pass
                

def solution(numbers, target):
    answer = 0
    nums = list(set(permutations(numbers)))
    plma = make_plma(len(numbers))
    for a in range(0, len(plma)):
        for i,j in zip(nums, plma[a]):
            print(i,j)
    
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3

solution(numbers, target)
#숫자와 기호의 모든 조합을 엮어서 계산하려고 함
#시간복잡도 최악