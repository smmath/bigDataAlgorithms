import random
from big_data_algorithms.util import int_stream, AlgorithmPrinter


def reservoir_sample(X, k, R=None):
    S = []
    r = 0

    printer = AlgorithmPrinter()

    for x, i in zip(X, int_stream()):
        if i <= k:
            S.append(x)
        else:
            r = random.uniform(0, 1) if R is None else R[i-1]
            if r <= k / i:
                S[(i-1) % k] = x

        printer.push_variable('i', i, 8)
        printer.push_variable('x_i', x, 12)
        printer.push_variable('r', r, 16)
        printer.push_variable('add?', (i <= k) | (r <= k / i), 16)
        printer.push_variable('S', S, 32)
        printer.print_step()

    return S
