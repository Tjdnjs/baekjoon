# 어떤 자연수 N : 작거나 같은 제곱수들의 합
# 제곱수들의 합을 표현할 때 그 항의 최소개수?

N = int(input())
result = [0 for _ in range(N+1)]

for i in range(1,N+1):
    x=[]
    for j in [x*x for x in range(1,int(i**0.5)+1)]:
        x.append(result[i-j])
    result[i]=min(x)+1

print(result[N])