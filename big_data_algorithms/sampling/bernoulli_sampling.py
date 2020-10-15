import random
import math
from big_data_algorithms.util import int_stream, AlgorithmPrinter


# With skip for efficiency
def bernoulli_sample(X, q, R=None):
    B = []
    m = __determine_skip(0, q, None if R is None else R[0])

    printer = AlgorithmPrinter()

    for (xi, i) in zip(X, int_stream()):
        m_ = m
        if i == m:
            B.append(xi)  # add the value to the sample
            m = __determine_skip(m_, q, None if R is None else R[i-1])

        printer.push_variable('i', i, 8)
        printer.push_variable('x_i', xi, 12)
        printer.push_variable('r_i', R[i-1] if R is not None else '', 16)
        printer.push_variable('m', m_, 8)
        printer.push_variable('skip?', i == m_, 16)
        printer.push_variable('B', B, 32)
        printer.print_step()

    return B


def __determine_skip(m, q, r):
    if r is None:
        U = random.random()
    else:
        U = r

    delta = math.ceil(math.log(U) / math.log(1 - q)) - 1
    return m + delta + 1


# naive implementation
def naive_bernoulli_sample(stream, q, R=None):
    B = []
    q = 0.3

    printer = AlgorithmPrinter()

    for xi, i in zip(stream, int_stream(0)):
        r = random.random() if R is None else R[i-1]
        if r <= q:
            B.append(xi)

        printer.push_variable('i', i, 8)
        printer.push_variable('x_i', xi, 12)
        printer.push_variable('r_i', r, 16)
        printer.push_variable('skip?', r > q, 16)
        printer.push_variable('B', B, 32)
        printer.print_step()

    return B