def calc_fib(n):
    if n<2:
        if n==1:
            return 1
        else:
            return 0
    else:
        f = [0]*(n+1)
        f[0] = 0
        f[1] = 1
        for i in range (2,n+1):
            f[i] = f[i-2]+f[i-1]
        return f[i]

n = int(input())
print(calc_fib(n))