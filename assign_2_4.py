


def lcm(a, b):
    if a == 1 or b == 1:
        return a*b
    else:
        i = min(a, b)
        j = max(a, b)
        while i != 0 and j != 0:
            r = j % i
            j = i
            i = r

        g = max(i, j)
        return int((a * b) / g)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

