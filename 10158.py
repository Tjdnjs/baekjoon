# 가로 w, 세로 h -> lowerleft (0,0)
# (p,q) 출발, 1시간 후 : (p+1, q+1) / 벽에 닿으면 반사되어 움직임
# wxh, p,q 출발, t시간 후 위치 (x,y)

import sys
input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

def loc(now , l):
    diraction = (now + t) // l
    index = (now + t) % l
    if diraction % 2 == 0:
        return index
    else:
        return (l - index)

print(loc(p,w), loc(q,h))