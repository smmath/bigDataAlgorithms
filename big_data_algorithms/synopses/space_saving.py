from big_data_algorithms.util import AlgorithmPrinter
import math


def space_saving(X, k):
    candidates = dict()

    printer = AlgorithmPrinter()
    print('FIRST PASS')

    for x in X:
        if x in candidates:
            candidates[x] += 1
        elif len(candidates) < k - 1:
            candidates[x] = 1
        else:
            min_k, min_v = min_key_value(candidates)
            candidates.pop(min_k)
            candidates[x] = min_v + 1

        printer.push_variable('x', x, 12)
        printer.push_variable('x in C?', x in candidates, 24)
        printer.push_variable('C', candidates, 32)
        printer.print_step()

    print('SECOND PASS')

    for c in candidates:
        candidates[c] = 0
    for x in X:
        if x in candidates:
            candidates[x] += 1
        printer.push_variable('x', x, 12)
        printer.push_variable('x in C?', x in candidates, 24)
        printer.push_variable('C', candidates, 32)
        printer.print_step()

    return candidates


def min_key_value(D):
    min_k = None
    min_v = math.inf
    for k, v in zip(D.keys(), D.values()):
        if v < min_v:
            min_k = k
            min_v = v
    return min_k, min_v
