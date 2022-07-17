n, m = map(int, input().split())

ppl = {}

for _ in range(n+m):
    x = input()
    if x in ppl.keys(): ppl[x] += 1
    else: ppl[x] = 1

result = sorted([x for x in ppl.keys() if ppl[x]==2])

print(len(result))
print(*result, sep="\n")