import numpy as np
def solution(n, left, right):
    square = [[0 for i in range(n)] for i in range(n)]
    answer = []
    for i in range(left//n, right//n+1):
        for j in range(0, i+1):
            square[j][i] = i+1
            square[i][j] = i+1
    
    print(square)
    # square = np.array(square)
    # square = square.reshape(-1,).tolist()
    # answer = square[left:right+1]
    
    
    return answer