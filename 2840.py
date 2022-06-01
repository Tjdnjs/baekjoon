# 행운의 바퀴, 시계방향으로 돌아가고 같은 글자가 한 번만 등장
# K번 돌리며, 화살표가 가리키는 글자가 변화는 횟수(S), 어떤 글자에서 회전을 멈추었는 지 적음
# 종이에 적은 내용, 바퀴의 칸 수 : 바퀴 알파벳 알아내기

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
wheel = [0]*N
turn = 0

for i in range(K):
    S, alpha = input().split()
    turn += int(S)
    if wheel[(N-turn%N)%N]==0:
        wheel[(N-turn%N)%N]=alpha
    elif wheel[(N-turn%N)%N]!=alpha:
        print('!')
        sys.exit()

for i in wheel:
    if i!=0 and wheel.count(i)>1:
        print('!')
        sys.exit()

last = (N-turn%N)
result = wheel[last:]+wheel[:last]
for i in range(N):
    if result[i]==0:
        print('?', end='')
    else:
        print(result[i], end='')