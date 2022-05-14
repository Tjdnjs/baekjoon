# 네 점, 정사각형 만들 수 있으면 1, 없으면 0
# 첫 줄 : 테스트케이스 개수, 한 줄에 한 점씩 네 점의 좌표

import sys
input = sys.stdin.readline
def distance(p1, p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)

T = int(input())

for _ in range(T):
    square = []
    for _ in range(4):
        x, y = map(int, input().split())
        square.append([x,y])
    square = sorted(square)
    if distance(square[0], square[1]) == distance(square[0], square[2]) == distance(square[2], square[3]) == distance(square[1], square[3]) and distance(square[0], square[3])==distance(square[1], square[2]):
        print(1)
    else:
        print(0)