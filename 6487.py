# 두 직선이 만나는 지 확인
'''
직선 1 : y = m1*x + y1
직선 2 : y = m2*x + y2
교점 x좌표 : -(y1-y2)/(m1-m2)
교점 y좌표 : m1*x + y1
'''
N = int(input())
line = []

for _ in range(N):
    line.append(list(map(int, input().split())))

for i in range(N):
    m1 = 0; m2 = 0; y1 = 0; y2 = 0;
    check1 = 0; check2 = 0;

    if line[i][0] == line[i][2]:
        check1 = line[i][0]
    else:
        m1 = (line[i][3]-line[i][1])/(line[i][2]-line[i][0])
        y1 = line[i][1] - m1*line[i][0]
    if line[i][4] == line[i][6]:
        check2 = line[i][4]
    else:
        m2 = (line[i][7]-line[i][5])/(line[i][6]-line[i][4])
        y2 = line[i][5] - m2*line[i][4]

    if check1 != 0 or check2 != 0:
        if check1 == check2:
            print('LINE')
        elif check1 != 0 and check2 != 0:
            print('NONE')
        else:
            if check1 != 0:
                print('POINT {0:.2f} {1:.2f}'.format(check1, m2*check1 + y2))
            elif check2 != 0:
                print('POINT {0:.2f} {1:.2f}'.format(check2, m1*check2 + y1))
    elif m1 == m2:
        if y1 == y2:
            print('LINE')
        else:
            print('NONE')
    else:
        x = -(y1-y2)/(m1-m2)
        y = m1*x + y1
        print('POINT {0:.2f} {1:.2f}'.format(x,y))