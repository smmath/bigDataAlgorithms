from big_data_algorithms.util import int_stream
from .kahan_sum import kahan_sum_internal


def one_pass_variance(stream):
    var = 0
    s = 0   # actual sum
    c = 0
    s2 = 0  # sum of (x - mu)**2
    mu = 0
    indicies = int_stream()
    for x, i in zip(stream, indicies):
        (s, c) = kahan_sum_internal(x, s, c)
        mu_ = s / i
        s2 = s2 + (x - mu) * (x - mu_)
        yield s2 / i