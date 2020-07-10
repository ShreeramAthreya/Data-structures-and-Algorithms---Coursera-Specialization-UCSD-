

def fibonacci_sum_squares_naive(n):
    r = n % 60
    if r <= 1:
        return r
    else:
        a = 0
        b = 1
        for i in range(1, r+1):
            s = (a + b) % 10
            a = b
            b = s

        return (a * b) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))
