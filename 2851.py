# 10개의 버섯, 나온 순서대로 집음
# 점수의 합 최대한 100에 가깝게

mush =[]
result=0

for _ in range(10):
    mush.append(int(input()))

for i in mush:
    result+=i
    if result>=100:
        if result-100>100-(result-i):
            result-=i
        break

print(result)