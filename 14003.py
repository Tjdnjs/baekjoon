from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

part = [num[0]]; dp = [0 for _ in range(n)]; length = 0

for i in range(1,n):
    if num[i] > part[-1]: part.append(num[i]); length += 1; dp[i] = length
    else: dp[i] = bisect_left(part, num[i]); part[dp[i]] = num[i]

print(length+1)
result = []
for i in range(n-1, -1, -1):
    if dp[i] == length: result.append(num[i]); length-=1

print(*result[::-1])