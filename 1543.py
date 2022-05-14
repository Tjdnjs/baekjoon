# 영어 문서 검색, 중복되지 않게 몇 번 등장하는 지

string = input()
find = input()
l = len(find)
i=0
cnt=0

while len(string)-i>=l:
    if string[i:i+l]==find:
        cnt+=1
        i+=l
    else:
        i+=1

print(cnt)