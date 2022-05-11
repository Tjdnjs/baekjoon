# 기호 1번이 당선되도록 사람을 매수
# 매수해야하는 사람의 최솟값
# 첫 줄 : 후보 수 N, 둘째 줄~ : n번을 찍으려는 사람 수

import sys
input = sys.stdin.readline

N = int(input())
dasom = int(input())
vote = []

for _ in range(N-1):
    vote.append(int(input()))
    
vote.sort(reverse = True)
cnt = 0

if N > 1:
    while(vote[0] >= dasom):
        dasom += 1
        vote[0] -= 1
        cnt += 1
        vote.sort(reverse = True)
        
print(cnt)