# 서로 다른 N 개의 자연수 합 S, S를 알 때 N의 최댓값?
# 1<=S<=4,324,967,295

S = int(input())
N = 0

while N<S:
    N += 1
    S -= N

print(N)