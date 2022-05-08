def Max(list):
    tmp=0
    index=0
    for i in range(len(list)):
        if list[i]>tmp:
            tmp=list[i]
            index=i
    return index

n = int(input())
stu_class = [list(map(int,input().split())) for _ in range(n)]
overlap = [0,0,0,0,0]

for i in range(n-1):
    for j in range(i+1,n):
        for k in range(5):
            if stu_class[i][k]==stu_class[j][k]:
                overlap[i]+=1
                overlap[j]+=1
                break

result = Max(overlap)            
print(result+1)
