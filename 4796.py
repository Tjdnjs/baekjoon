# 연속하는 P일 중 L일동안 사용, V일 휴가
# 최대 며칠?
# 여러 개,  LPV 순서, 마지막 줄 0 0 0

camp = []
i=1
while True:
    L, P, V = map(int, input().split())
    if L+P+V==0:
        break;
    camp.append([i, L, P, V])
    i+=1

for j in camp:
    result = (j[3]//j[2])*j[1]
    if j[3]%j[2]>j[1]:
        result+=j[1]
    else:
        result+=j[3]%j[2]
    print("Case %d: %d" %(j[0],result))