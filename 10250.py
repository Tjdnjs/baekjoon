"""
입력 : T테스트케이스 , HWN -> 층 수, 방 수, 몇 번째 손님
"""
# 층 수 : n%h, 방 번호 : n//h+1

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h == 0: print(h*100+n//h); continue
    print((n%h)*100+(n//h+1))