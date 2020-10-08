import random
import math


# With skip for efficiency
def bernoulli_sample(x, n=None):
    if n == None:
        n = len(x)

    newX = []
    q = 0.3;  # the bernoulli sampling rate
    m = 0  # index of the next element to be included
    i = 0;  # counter

    # determines the initial skip amount
    U = random.random();
    tri = math.log(U) / math.log(1 - q) - 1;
    m = tri + 1;

    for xi in x:
        if i > n:
            break

        if i == int(
                m):  # add value to the sample. Must convert m to int otherwise it is a decimal which i, the counter, is not

            newX.append(xi);  # add the value to the sample

            U = random.random();  # generate new random

            tri = math.log(U) / math.log(1 - q) - 1  # calculate the tri for the next skip value

            m = m + tri + 1;  # determines next skip value

        i += 1

    return newX;


# naive implementation
def naive_bernoulli_sample(x):
    newX = []
    q = 0.3

    for xi in x:
        r = random.random();

        if r <= q:
            newX.append(xi)

    return newX;