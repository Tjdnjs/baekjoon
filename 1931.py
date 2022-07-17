import sys
input = sys.stdin.readline
N = int(input())
tmp = []
for _ in range(N):
    tmp.append(list(map(int, input().split())))

x = 0; cnt = 0; 
tmp = sorted(tmp, key = lambda x:(x[1],x[0]))

for i in range(N):
    if tmp[i][0]>=x:
        cnt+=1
        x = tmp[i][1]
print(cnt)