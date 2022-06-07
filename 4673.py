# d(n) 은 n과 n의 각 자리수를 더하는 함수
# ex) d(75) = 75 + 7 + 5 = 87
# d(n), d(d(n)) ,,, 무한수열, 생성자가 없는 숫자 = 셀프 넘버
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력 (입력 x)

all = set(range(1,10001))
non = set()

for i in range(1,10001):
    for j in str(i):
        i+=int(j)
    non.add(i)

self = all-non

for i in sorted(self):
    print(i)
