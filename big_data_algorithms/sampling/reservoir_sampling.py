import random
from big_data_algorithms.util import int_stream


def reservoir_sample(X, k, n):
    indices = int_stream()
    S = []
    for x, i in zip(X, indices):
        if i > n:
            break

        if i <= k:
            S.append(x)
            continue

        r = random.uniform(0, 1)
        if r <= k / i:
            S[i % k] = x

    return S
