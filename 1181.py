# 1<=N<=20,000 개의 단어를 1. 길이 짧은 순, 2. 사전 순 으로 정렬
# 같은 단어가 여러 번 입력된 경우에는 한 번만

import sys
input = sys.stdin.readline

N = int(input())
word = set()
for _ in range(N):
    word.add(input().strip())

word = list(word)
word.sort(key = lambda x : (len(x), x))

for i in word:
    print(i)