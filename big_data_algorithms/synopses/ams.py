import random


def ams(stream, s, n):
    p = set(random.sample(range(0, n - 1), s))
    c = dict()
    for i, x in enumerate(stream):
        if i in p:
            c[x] = 0
        if x in c:
            c[x] = c[x] + 1

    return (n / s) * sum(map(lambda j: 2 * j - 1, c.values()))
