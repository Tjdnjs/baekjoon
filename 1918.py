import sys
input = sys.stdin.readline

x = input().strip()
result = []; stk = []

for i in x:
    if i == '(': stk.append(i)
    elif i == ')':
        while stk and stk[-1] != '(': result.append(stk.pop())
        stk.pop()
    elif i in '*/':
        if not stk: stk.append(i)
        else:
            while stk and stk[-1] in '*/': result.append(stk.pop())
            stk.append(i)
    elif i in '+-':
        if not stk: stk.append(i)
        else:
            while stk and stk[-1] in '+-*/': result.append(stk.pop())
            stk.append(i)
    else: result.append(i)

result += stk[::-1]; print(*result, sep="")