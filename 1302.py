# 첫 줄 : N, 둘쩨 줄 : N개의 줄에 책의 제목
# 가장 많이 팔린 책의 제목, 가장 많이 팔린 책이 여러 개 : 사전 순

N = int(input())
book = {}

for _ in range(N):
    B = input()
    if B not in book:
        book[B] = 1
    else:
        book[B] += 1

book = sorted(book.items(), key = lambda x: (-x[1], x[0]))

print(book[0][0])