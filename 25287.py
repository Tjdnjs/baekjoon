import sys
input = sys.stdin.readline

def yesorno():
    N = int(input());
    num = list(map(int, input().split()));
    mid = N//2 if N%2==0 else N//2+1
    idx = num.index(mid)
    num[0] = min(num[0], N-num[0]+1)
    for i in range(1, idx):
        num[i] = min(num[i], N-num[i]+1)
        if num[i] < num[i-1] : return 0;
    for i in range(idx+1, N):
        num[i] = max(num[i], N-num[i]+1)
        if num[i] < num[i-1] : return 0;
    return 1;
        
for _ in range(int(input())):
    if yesorno(): print('YES')
    else: print('NO')