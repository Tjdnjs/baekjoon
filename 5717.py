# 남자 친구의 수와 여자 친구의 수가 주어졌을 때, 친구는 총 몇 명

while True:
    M, F = map(int, input().split())
    if M == 0 and F == 0 : break
    print(M+F)