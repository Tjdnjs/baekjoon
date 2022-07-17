def isprime(a):
    if a == 1: return 0
    for i in range(2,a):
        if a%i == 0: return 0
    return 1

cnt = 0

n = int(input())
num = list(map(int, input().split()))
for i in num:
    if isprime(i)==1: cnt += 1;
    else: continue

print(cnt)