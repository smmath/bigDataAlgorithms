def kahan_sum_internal(x, s, c):
    y = x - c
    t = s + y
    c = (t - s) - y
    s = t
    return (s, c)


def kahan_sum(stream):
    s = 0
    c = 0
    for x in stream:
        (s, c) = kahan_sum_internal(x, s, c)
        yield s