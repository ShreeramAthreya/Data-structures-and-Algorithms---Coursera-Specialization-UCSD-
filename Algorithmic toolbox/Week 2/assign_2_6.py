
def fibonacci_sum_naive(n):
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
            suum = (suum + (s % 10)) % 10
        return suum


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_naive(n))
