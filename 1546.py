# 점수 중 최댓값 M, 모든 점수 = 점수/M*100
# 새로운 평균 / 첫 줄 : 과목 개수 N, 둘째 줄 : 점수

N = int(input())
score = list(map(int, input().split()))
    
M = max(score)

for i in range(N):
    score[i]/=(M*0.01)

print(sum(score)/N)