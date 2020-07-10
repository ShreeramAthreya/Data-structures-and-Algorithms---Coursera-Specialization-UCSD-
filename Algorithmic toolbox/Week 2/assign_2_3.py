
def gcd_naive(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        i = min(a, b)
        j = max(a, b)
        while i != 0 and j != 0:
            r = j % i
            j = i
            i = r

    return max(i, j)

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd_naive(a, b))