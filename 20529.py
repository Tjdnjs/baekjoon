import sys
input = sys.stdin.readline
from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    mbti = list(map(str, input().strip().split()))
    if  n> 32: print(0); continue;
    sel_3 = list(combinations(mbti,3))
    ans = 8
    for i in sel_3:
        cnt = 0;
        tmp1, tmp2, tmp3 = i[0], i[1], i[2]
        for j in range(4):
            if tmp1[j] == tmp2[j] == tmp3[j]: continue
            else: cnt += 2
        ans = min(ans,cnt)
    print(ans)