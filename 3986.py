# A와 B로 이루어진 단어, 좋은 단어의 개수?
# 같은 글자끼리 쌍을 지었을 때 선끼리 교차하지 않으면 좋은 단어

import sys
input = sys.stdin.readline

N = int(input())
cnt=0

for _ in range(N):
    word = input().strip()
    while(word.count("AA")>0 or word.count("BB")>0):
        word = word.replace('AA','').replace('BB','')
    if len(word)==0:
        cnt+=1
print(cnt)