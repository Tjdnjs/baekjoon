# 첫 줄 : 집합 A, 집합 B의 원소 개수
# 둘째 줄 : 집합 A의 모든 원소
# 셋째 줄 : 집합 B의 모든 원소

import sys
input = sys.stdin.readline

nA , nB = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B)+len(B-A))