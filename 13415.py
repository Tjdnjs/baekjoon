import sys
from collections import deque

input = sys.stdin.readline

n = int(input()); num = list(map(int, input().split()))
k = int(input()); dq = deque()

for _ in range(k):
    a, b = map(int, input().split())
    while dq and abs(dq[len(dq)-1]) <= a: dq.pop()
    dq.append(a)
    while dq and abs(dq[len(dq)-1]) <= b: dq.pop()
    dq.append(-b)

result = deque(); dq.append(0); idx = abs(dq[0])
x = deque(sorted(num[:idx]))

for _ in range(len(dq)-1):
    cmd = dq.popleft()
    if cmd > 0:
        for _ in range(abs(cmd)-abs(dq[0])): result.appendleft(x.pop())
    else:
        for _ in range(abs(cmd)-abs(dq[0])): result.appendleft(x.popleft())

result += num[idx:]; print(*result)