# 포켓몬 개수 N, 맞춰야하는 문제 개수 M (N,M:1~100000)
# 둘째 줄 N개의 줄에 1~N번 포켓몬 한 줄에 하나씩 입력
# 이름: 영어, 첫 글자 or 마지막 글자만 대문자(2~20)
# M개의 줄에 문제 : 알파벳-번호, 숫자-문자 출력

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
pokemon = {}

for i in range(N):
    name = input().strip()
    pokemon[name]=str(i+1)
    pokemon[str(i+1)]=name

for _ in range(M):
    print(pokemon[input().strip()])