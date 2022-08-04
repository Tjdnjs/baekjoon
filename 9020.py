import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 2: return 1
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0: return False
        return True

for _ in range(int(input())):
    num1 = int(input())//2; num2 = num1;
    while 1:
        if isPrime(num1) and isPrime(num2): print(num1, num2); break;
        else: num1 -= 1; num2 += 1;