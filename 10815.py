# 카드 N개, 정수 M개, 있는 지 아닌 지

import sys
input = sys.stdin.readline

N = int(input())
N_set = set(map(int, input().split()))

M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    if i in N_set:
        print(1, end = ' ')
    else:
        print(0, end = ' ')