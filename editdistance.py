import functools

def edit_dyn(above, below):
    m = len(above)
    n = len(below)
    d = [[0 for y in range(n + 1)] for x in range(m + 1)]
    a = [[0 for y in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        d[i][0] = i
        a[i][0] = 3
    for j in range(n + 1):
        d[0][j] = j
        a[0][j] = 2
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if above[i-1] == below[j-1]:
                d[i][j] = d[i-1][j-1]
                a[i][j] = 0
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
                if d[i][j] == d[i-1][j-1] + 1:
                    a[i][j] = 1
                elif d[i][j] == d[i][j-1] + 1:
                    a[i][j] = 2
                else:
                    a[i][j] = 3

    for line in d:
        print(line)
    print()
    for line in a:
        print(line)
    #print(d)
    #print(a)

    b = ""
    c = ""

    distance = 0
    while(m > 0 and n > 0):
        if a[m][n] == 0 or a[m][n] == 1:
            b += above[m-1]
            c += below[n-1]
            m -= 1
            n -= 1
            if a[m][n] == 1:
                distance += 1
        elif a[m][n] == 2:
            b += "-"
            c += below[n - 1]
            n -= 1
            distance += 1
        elif a[m][n] == 3:
            b += above[m-1]
            c += "-"
            m -= 1
            distance += 1

    b = b[::-1]
    c = c[::-1]
    print(b)
    print(c)
    print(distance)

@functools.lru_cache(maxsize = 800)
def edit_rec(s, t):
    m = len(s)
    n = len(t)
    print(s)
    print(t)
    if n == 0:
        print("t is done")
        return m
    elif m == 0:
        print("s is done")
        return n
    elif s[m-1] == t[n-1]:
        print("Same")
        return edit_rec(s[:m-1], t[:m-1])
    else:
        tack = min(edit_rec(s[:m-1], t[:n-1]),
                   edit_rec(s[:m], t[:n-1]),
                   edit_rec(s[:m-1], t[:n]))
        print("tack", tack)
        return 1 + tack
    
