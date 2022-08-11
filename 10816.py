import sys
input = sys.stdin.readline

n = int(input())
sang = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
dic = {}
for i in sang:
    if i in dic: dic[i] += 1
    else: dic[i] = 1
print(" ".join(str(dic[j]) if j in dic else '0' for j in num))