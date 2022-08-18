import heapq
import sys
input = sys.stdin.readline

heap = []

for _ in range(int(input())):
    x = int(input()) # 자연수라면 배열에 x 추가, 0이면 가장 작은 값 출력 -> 제거
    if x!= 0 : heapq.heappush(heap, (abs(x), x))
    else : 
        if heap == [] : print(0)
        else: print(heapq.heappop(heap)[1])