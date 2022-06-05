# 세 점이 주어졌을 때, 축에 평행한 직사각형, 네번째 점?

x = [0 for _ in range(3)]
y = [0 for _ in range(3)]

for i in range(3):
    x[i], y[i] = map(int, input().split())

for i in range(3):
    if x.count(x[i])==1:
        xx = x[i]
    if y.count(y[i])==1:
        yy = y[i]

print(xx, yy)