# (), [], 사이 문자열 - 올바른 지
# 입력종료 : .
# yes, no 출력
import sys
import re
input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string=='.':
        break
    else:
        PS = re.sub('[a-zA-Z0-9\s]','',string)
        for i in range(len(PS)):
            PS = PS.replace('()','').replace('[]','').replace('.','')
        if len(PS)==0:
            print('yes')
        else:
            print('no')