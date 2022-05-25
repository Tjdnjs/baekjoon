# 0~N까지의 정수 K개 그 합이 N이 되는 경우의 수
# 덧셈의 순서가 바뀐 경우는 다른 경우

from math import comb
N, K = map(int, input().split())
print(comb(K+N-1,N)%(10**9))