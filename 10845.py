from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push': dq.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(dq) == 0 : print(-1)
        else: print(dq.popleft())
    elif cmd[0] == 'size': print(len(dq))
    elif cmd[0] == 'empty': print(int(len(dq)==0))
    elif cmd[0] == 'front':
        if len(dq) == 0: print(-1)
        else: print(dq[0])
    elif cmd[0] == 'back':
        if len(dq) == 0: print(-1)
        else: print(dq[-1])