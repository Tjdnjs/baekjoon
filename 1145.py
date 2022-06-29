# 다섯 개의 자연수, 대부분의 배수 : 적어도 세 개로
# 작은 수

'''num = list(map(int, input().split()))
num.sort()
for i in range(1,10**6+1):
    cnt = 0
    for j in num:
        if i % j == 0: cnt += 1
        if cnt == 3:
            print(i)
            exit(0)'''

num = list(map(int, input().split()))

def gcd(a, b): 
	if a<b: a,b = b,a 
	if a%b==0: return b 
	else: return gcd(b, a%b)

def lcm(a, b):  # 최소 공배수
    try:
        return (a * b) // gcd(a, b)
    except:
        return 0


result = 10 ** 6

for i in range(3):  # 0~2까지와
    for j in range(i + 1, 4):  # i+1부터 4까지와
        for k in range(j + 1, 5):  # j+1 부터 5까지
            result = min(result, lcm(lcm(num[i], num[j]), num[k]))  # 3개의 숫자에 대한 최소 공배수
print(result)