# Uses python3
import sys


def fibo(n):
    a = 0
    b = 1
    suum = 1
    r = n % 60
    if r <= 1:
        return r
    else:
        for i in range(1, r):
            s = a + b
            a = b
            b = s
            suum = suum + s
        return suum

def get_fibonacci_last_digit_naive(n):
    r = n % 60
    if r <= 1:
        return r
    else:
        a = 0
        b = 1
        for i in range(1, r):
            s = (a + b) % 10
            a = b
            b = s
        return s

if __name__ == '__main__':
    m, n = map(int, input().split())
    if m == n:
        print(get_fibonacci_last_digit_naive(m))
    else:
        ans = (fibo(n) - fibo(m-1)) % 10
        print(ans)
