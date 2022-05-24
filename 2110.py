# 집 N개가 수직선 위에, C개의 공유기
# 가장 인접한 공유기 사이의 최대 거리 출력

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
x = sorted([int(input()) for _ in range(N)])

start, end = 1, (x[-1]-x[0])//(C-1)+1
result = 0

while start<=end:
    mid = (start+end)//2
    cnt = 1
    cur = x[0]
    for i in range(1,N):
        if x[i]-cur >= mid:
            cnt += 1
            cur = x[i]
          
    if cnt >= C:
        start = mid +1
        result = mid
    else:
        end = mid-1

print(result)