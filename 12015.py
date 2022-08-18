import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
tmp = [0]

for i in range(n):
    start = 0; end = len(tmp)-1;
    while end-start >= 0:
        mid = (start+end) // 2
        if tmp[mid] < num[i]: start = mid+1;
        else: end = mid-1
    if start >= len(tmp): tmp.append(num[i])
    else: tmp[start] = num[i]

print(len(tmp)-1)

"""
N = int(input())
array= list(map(int,input().split()))
result = [1]* N 
for i in range(1,N):
    for j in range(i):
        if array[j] < array[i]:
            result[i] = max(result[i],result[j]+1)
print(max(result))
"""