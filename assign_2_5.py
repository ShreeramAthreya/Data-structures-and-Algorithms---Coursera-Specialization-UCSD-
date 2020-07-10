# Uses python3


def get_fibonacci_huge_naive(n, m):

    if n <= 1:
        return n
    else:
        k=0
        a = 0
        b = 1
        bo = 0
        while bo != 1:
            s = a + b
            a = b
            b = s
            t = s % m
            k = k + 1
            if t == 0 and k > 1:
                if (a + b) % m == 1:
                    bo = 1
        r = n % (k+1)
        print(k+1)
        if r <= 1:
            return r
        else:
            f = [0]*(r+1)
            f[0] = 0
            f[1] = 1
            for i in range(2, r+1):
                ans = f[i - 2] + f[i - 1]
                f[i] = ans % m
            return f[i]


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge_naive(n, m))
