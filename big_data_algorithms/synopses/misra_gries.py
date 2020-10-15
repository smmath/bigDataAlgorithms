from big_data_algorithms.util import AlgorithmPrinter


def misra_gries(X, k):
    candidates = dict()
    printer = AlgorithmPrinter()
    print('FIRST PASS')

    for x in X:
        if x in candidates:
            candidates[x] += 1
        elif len(candidates) < k - 1:
            candidates[x] = 1
        else:
            for c in list(candidates.keys()):
                candidates[c] -= 1
                if candidates[c] == 0:
                    candidates.pop(c)
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
