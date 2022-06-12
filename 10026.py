# N*N 그리드, RGB 그림
# 적록색약이 아닌 사람과 적록색약인 사람이 봤을 때 구역의 수

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
photo = []

for _ in range(N):
    photo.append(list(map(str, input().strip())))

visited = [[0]*N for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    deque().append((x,y))
    visited[x][y] = 1

    while deque():
        x, y = deque().popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<N and 0<=ny<N and photo[x][y]==photo[nx][ny] and visited[nx][ny]==0:
                deque().append((nx,ny))
                visited[nx][ny] = 1

count = [0, 0]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            bfs(i,j)
            count[0]+=1

visited = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if photo[i][j]=='G':
            photo[i][j]=='R'

for i in range(N):
    for j in range(N):
        if visited[i][j]==0:
            bfs(i,j)
            count[1]+=1

for i in count:
    print(i, end = ' ')