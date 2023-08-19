from collections import deque

def diff(word1, word2):
    count = 0
    for i in range(0, len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count

def makeDict(begin, words):
    word_dict = {}
    if (target in words) == False:
        answer = 0
        return answer
    
    word_dict[begin] = []
    for i in words:
        word_dict[i] = []
    
    for i in words:
        if diff(begin, i) == 1:
            word_dict[begin].append(i)
            
        for j in words:
            if diff(i, j) == 1:
                word_dict[i].append(j)
                
    return word_dict

def bfs(dict, begin, target, words):
    queue = deque()
    count = 0 
    path = []
    path.append(begin)
    queue.append(begin)
    words.remove(begin)
    
    while queue:
        current = queue.popleft()
        if current == target:
            return count
        
        else:
            for i in dict[current]:
                if i not in words:
                    continue
                
                else:
                    queue.append(i)
                    path.append(i)
                    words.remove(i)
                    count += 1
    
    print(path)
    return count
                
    
    
    

def solution(begin, target, words):
    answer = 0
    copy_word = words[:]
    copy_word.insert(0, begin)
    word_dict = makeDict(begin, words)
    
    answer = bfs(word_dict, begin, target, copy_word)
    print(answer)
    return answer

target = "cog"
begin = "hit"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

solution(begin, target, words)