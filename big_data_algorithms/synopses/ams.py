import random
from big_data_algorithms.util import AlgorithmPrinter


def ams_algorithm(stream, s, n, P=None):
    P = set(random.sample(range(0, n), s)) if P == None else P
    C = dict()
    printer = AlgorithmPrinter()
    for i, x in enumerate(stream):
        if i in P:
            C[x] = 0
        if x in C:
            C[x] += 1
        printer.push_variable('i', i, 8)
        printer.push_variable('x_i', x, 12)
        printer.push_variable('i in P?', i in P, 24)
        printer.push_variable('C', C, 32)
        printer.print_step()

    return (n / s) * sum(map(lambda c: 2 * c - 1, C.values()))


def actual_m2(stream):
    C = dict()
    for i, x in enumerate(stream):
        if x in C:
            C[x] += 1
        else:
            C[x] = 1

    return sum(map(lambda c: c**2, C.values()))
