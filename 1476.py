# 1<=E<=15, 1<=S<=28, 1<=M<=19
# E, S, M 이 주어질 때, 몇 년인 지

year = 1

E, S, M = map(int, input().split())

while True:
    if (year-E)%15==0 and (year-S)%28==0 and (year-M)%19==0:
        print(year)
        break
    year+=1