# R행 C열 S로 시작 F가 끝
# 9팀, 결승선으로부터 떨어진 거리로 측정
# 두 팀이 거리가 같으면, 같은 등수

R, C = map(int, input().split())
kayak = [input() for _ in range(R)]
grade = 1
result = [0]*10

for j in range(C-2, 1, -1):
    checker = 0
    for i in range(R):
        if kayak[i][j] != '.' and result[int(kayak[i][j])]==0:
            result[int(kayak[i][j])]=grade
            checker = 1
    if checker == 1:
        grade += 1

for i in result:
    if i != 0: print(i)