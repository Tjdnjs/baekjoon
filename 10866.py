from collections import deque
import sys
input = sys.stdin.readline

dq = deque()
n = int(input())

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push_front': dq.appendleft(cmd[1])
    elif cmd[0] == 'push_back': dq.append(cmd[1])
    elif cmd[0] == 'pop_front':
        if len(dq) == 0 : print(-1)
        else: print(dq.popleft())
    elif cmd[0] == 'pop_back':
        if len(dq) == 0 : print(-1)
        else: print(dq.pop())
    elif cmd[0] == 'size': print(len(dq))
    elif cmd[0] == 'empty': print(int(len(dq)==0))
    elif cmd[0] == 'front':
        if len(dq) == 0: print(-1)
        else: print(dq[0])
    elif cmd[0] == 'back':
        if len(dq) == 0: print(-1)
        else: print(dq[-1])

"""
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
        
"""