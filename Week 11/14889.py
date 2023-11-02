from itertools import combinations
from itertools import permutations
import sys; input=sys.stdin.readline
n=int(input())
arr=[i for i in range(n)]
comb=list(combinations(arr,n//2)) #선수 조합
players=[]
for i in range(n):
    players.append(list(map(int,input().split()))) #점수 받아주기
ans=2000
for x in range(len(comb)//2): # 절반까지만
    start,link=0,0 # start,link의 값들을 저장할 변수
    for a,b in list(permutations(comb[x],2)): # permuatation을 이용해서 구해주도록 다 더해주기
        start+=players[a][b]
    for a,b in list(permutations(list(set(arr)-set(comb[x])),2)): 
        link+=players[a][b]
    ans=min(abs(start-link),ans) # 절댓값으로 최솟값 구하기
print(ans)