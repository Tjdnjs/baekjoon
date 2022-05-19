# 첫 줄 N : N개의 정수, 둘째 줄 M, M개의 수
# M~의 수가 N ~ 안에 존재하면 1, 아니면 0 M개의 줄에 출력

import sys
input = sys.stdin.readline

N = int(input())
'''
list로 선언한 A를 set 형식으로 바꾸니, 시간초과가 해결되었다
list의 search는 순차탐색이지만, set의 search는 순차탐색과정 없이 바로 진행된다
'''
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

for i in B:
    if i in A:
        print(1)
    else:
        print(0)