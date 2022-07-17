import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listen = set()
saw = set()

for _ in range(n): listen.add(input().strip())
for _ in range(m): saw.add(input().strip())

result = list(listen&saw); result.sort()

print(len(result)); print(*result, sep="\n")