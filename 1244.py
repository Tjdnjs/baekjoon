# 1 켜짐, 0 꺼짐
# 남학생 - 배수, 여학생 - 스위치를 중심으로 좌우의 상태가 대칭, 가장 많은 스위치를 포함하는 구간
# 첫 줄 : 스위치 개수, 둘째 줄 : 스위치 상태, 셋째 줄 : 학생 수
# 넷째 줄 : 성별, 받은 수 - 남 1, 여 2
# 20개씩 출력

N = int(input())
state = [-1]+list(map(int, input().split()))
stu_n = int(input())

for _ in range(stu_n):
    gender, index = map(int, input().split())
    if gender==1:
        for i in range(index, N+1, index):
            if state[i]==0:
                state[i]=1
            else:
                state[i]=0
    else:
        if state[index]==0:
            state[index]=1
        else:
            state[index]=0
        for i in range(1,min(index, N-index)+1):
            if state[index-i]!=state[index+i]:
                break
            else: 
                if state[index-i]==0 and state[index+i]==0:
                    state[index-i], state[index+i] = 1, 1
                else:
                    state[index-i], state[index+i] = 0, 0

for i in range(N//20+1):
    print(*state[20*i+1:20*(i+1)+1], sep=' ')