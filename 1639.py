# 행운의 티켓 : 2N자리로 이루어짐, 왼쪽 오른쪽 N개 수 합이 일치
# 연속된 부분 중 규칙 만족하는 최대부분 문자열 길이 출력
# 첫째 줄 : 문자열 S, 찾을 수 없으면 0 출력

S = input()
cnt=0

for i in range(len(S)-1):
    left = i
    right = i+1
    sum1, sum2 = 0, 0
    while left >= 0 and right < len(S):
        sum1 += int(S[left])
        sum2 += int(S[right])
        if sum1 == sum2:
            if cnt < right-left+1:
                cnt = right-left+1
        left -= 1
        right += 1

print(cnt)