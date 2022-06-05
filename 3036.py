# 링 N개, 링이 돌 대 나머지도 같이 돈다
# 링의 반지름, 첫 링 한바퀴 -> 나머지 몇 바퀴, 기약분수 출력

def gcd(a,b):
    for i in range(min(a,b), 0, -1):
        if a%i==0 and b%i==0:
            return i

N = int(input())
ring = list(map(int, input().split()))

first = ring[0]

for r in ring[1:]:
    x = gcd(first, r)
    print(f'{first//x}/{r//x}')