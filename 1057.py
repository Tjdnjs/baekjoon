'''
n명이 참가하는 토너먼트
1-n 배정, 인접한 번호끼리 / 이긴 사람 진출
다음 라운드에서 다시 참가자의 번호를 1번부터 (처음 순서 유지)
한 명만 남을 때까지
첫 줄 : 100000>=N>=2, K, L
둘이 몇 라운드에서 대결하는 지
'''
import math
import sys
input = sys.stdin.readline
cnt =0

N, K, L = map(int, input().split())

while K!=L:
    K = math.trunc(K/2+0.5)
    L = math.trunc(L/2+0.5)
    cnt+=1

print(cnt)