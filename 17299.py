import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
result = [-1]*n

cnt = [0]*1000001
for i in num: cnt[i] += 1

stk = []
for i in range(n):
    while stk:
        if cnt[num[stk[-1]]] < cnt[num[i]]: result[stk.pop()] = num[i]
        else: stk.append(i); break
    if not stk: stk.append(i)

print(*result)