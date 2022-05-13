# 정수 X 3의 배수 : 3으로 나눔 / 2의 배수 : 2로 나눔 / 1을 뺌
# 연산 세 개를 사용해서 1을 만듦
# 연산을 사용하는 횟수의 최소?

N = int(input())
dic = {1:0, 2:1}

def result(N):
    if N not in dic:
        dic[N] = (1 + min(result(N//3) + N%3, result(N//2) + N%2))
    return dic[N]

print(result(N))