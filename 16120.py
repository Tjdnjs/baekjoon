"""
PPAP 에서 P를 PPAP로 바꾸는 과정 -> PPAP / NP
"""

import sys
input = sys.stdin.readline

x = list(input().strip())

if x == 'P' or x == 'PPAP' : print('PPAP')
else:
    check = list("PPAP"); stk=[]
    for i in x: 
        stk.append(i)
        if stk[-4:] == check: stk.pop();stk.pop();stk.pop();
    if stk == check or stk == ['P']: print('PPAP')
    else: print('NP')