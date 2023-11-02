#빙산
from collections import deque 
n, m = list(map(int, input().split()))

ice = [[list(map(int, input().split()))] for i in range(n)]
visited = [[0]*m for _ in range(n)]

dx= [0,0,-1,1]
dy= [1,-1,0,0]

queue = deque()

def bfs():

#칸에 붙어있는 0의 개수만큼 감소
# 2덩이로 떨어지는 시간