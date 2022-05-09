# 1 2 2 3 3 3 4 4 4 4 .... 수열
# A부터 B번째 숫자까지의 합 구하기

A, B = map(int, input().split())

num=[]

for i in range(1,46):
    num+=[i]*i

print(sum(num[A-1:B]))