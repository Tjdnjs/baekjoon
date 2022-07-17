# 첫 줄 테케 수 C, 둘째 줄 - 학생의 수 N이 첫 수, N명의 점수.
# 평균이 넘는 학생의 비율 반올림 하여 소수점 셋째자리까지

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    score = list(map(int, input().split()))
    n, cnt = score[0], 0
    avg = (sum(score)-n)/n

    for i in range(1,n+1):
        if score[i] > avg: cnt += 1
    print("%.3f%%" %(cnt*100/n))