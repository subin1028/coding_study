from collections import deque

def diff(word1, word2):
    count = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            count += 1
            
    if count == 1:
        return True
    return False
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    def bfs():
        queue = deque()
        queue.append([0, begin])
        
        while queue:
            count, word = queue.popleft()
            
            for next_word in words:
                if diff(word, next_word):
                    if next_word == target:
                        return count + 1
                    
                    else:
                        queue.append([count+1, next_word])
                    
    answer = bfs()
    print(answer)
    return answer

target = "cog"
begin = "hit"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)