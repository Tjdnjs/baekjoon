# N개의 수가 주어졌을 때, 산술평균, 중앙값, 최빈값, 범위

import sys
input = sys.stdin.readline

N = int(input())

cnt = [0]*8001
max_lst = []
num = []

for _ in range(N):
    cnt[int(input())]+=1

max_cnt = max(cnt)

for i in range(-4000,4001):
    if cnt[i]==max_cnt:
        max_lst.append(i)
    for _ in range(cnt[i]):
        num.append(i)

#산술평균
print(round(sum(num)/N))
#중앙값
print(num[N//2])
#최빈값
if len(max_lst) >= 2:
    print(max_lst[1])
else:
    print(max_lst[0])
#범위
print(num[-1]-num[0])