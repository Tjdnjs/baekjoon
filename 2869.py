# 높이 V인 나무, 낮에 A미터 올라가고 밤에 B미터 미끄러짐
# 며칠이 걸리는 지, 첫 줄 : A, B, V 순서

import math

A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))