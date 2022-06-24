# x1,y1, x2,y2가 주어지고, 각각의 거리 r1, r2
# 류재명이 있을 수 있는 좌표의 수?, 무한대일 때 -1
# 첫 줄 테스트케이스 T

import math

T = int(input())

# 원 - 중심 사이 거리 계산, 반지름 비교
for _ in range(T):
    x1, y1, r1, x2,y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2)**0.5
    if d == 0 and r1 == r2 :
        print(-1)
    elif abs(r1-r2) == d or r1 + r2 == d:
        print(1)
    elif abs(r1-r2) < d and d < (r1+r2):
        print(2)
    else:
        print(0)