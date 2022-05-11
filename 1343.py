# AAAA, BB를 무한개 가지고 있다
# X와 . 으로 이루어진 보드판 - 겹침 없이 X를 폴리오미노로 덮을 것
# 모두 덮은 보드판 (사전 가장 앞서는 답) 출력

board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)