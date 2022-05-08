# 첫 줄에 주어지는 대문자 문자열
# 팰린드롬 만들기, 불가능 : I'm Sorry Hansoo 출력
# 답이 여러 개 : 사전 순으로 앞서는 것 

import sys
input = sys.stdin.readline

name = list(map(str, input().strip()))
l = ''
mid=''
cnt = [0 for _ in range(26)]
odd = 0

for i in name:
    cnt[ord(i)-65] += 1

for i in range(26):
    if cnt[i] % 2 == 1:
        odd += 1
        mid = chr(i+65)
    l+=chr(i+65) * (cnt[i] // 2)

r = list(l)
r.reverse()

if odd > 1:
    print("I'm Sorry Hansoo")
else:
    print(l + mid + ''.join(map(str, r)))