from big_data_algorithms.util import int_stream


class BloomFilter:
    def __init__(self, hash_functions, m):
        self.hash_functions = hash_functions
        self.k = len(hash_functions)
        self.m = m
        self.n = 0
        self.B = [0] * m

    def __create_filter(self):
        B = [0 for i in range(self.m)]
        for s, i in zip(self.S, int_stream(0)):
            for h in self.hash_functions:
                if h(s) == i:
                    B[i] = 1
        return B

    def insert(self, x):
        for h in self.hash_functions:
            self.B[h(x) % self.m] = 1
        self.n += 1

    def insert_all(self, X):
        for x in set(X):
            self.insert(x)

    def test_membership(self, x):
        return all([self.B[h(x)] == 1 for h in self.hash_functions])

    def filter(self, X):
        return [x for x in X if self.test_membership(x)]

    def false_positive_rate(self):
        return (1.0 - ((1.0 - 1.0/self.m)**(self.k*self.n))) ** self.k
