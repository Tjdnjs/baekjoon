"""
T / 함수 p : R 뒤집기, D 버리기/ 배열의 수 n / 정수
"""

from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cmd = list(input().rstrip()); n = int(input())
    dq = deque(input().rstrip().strip(']').strip('[').split(','))
    cnt_r, cnt_d = 0, 0
    result = ""
    for i in cmd:
        if i == 'R': cnt_r += 1
        elif i == 'D': 
            if dq == deque([]) or dq == deque(['']): result = 'error'
            else:
                if cnt_r%2 == 0: dq.popleft()
                else: dq.pop()
    if cnt_r % 2 == 1: dq.reverse()
    if result != 'error': result = "["+",".join(dq)+"]"
    print(result)