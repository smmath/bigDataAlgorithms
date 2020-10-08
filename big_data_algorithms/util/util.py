import random


def gauss_stream(mu, sigma):
    while True:
        yield random.gauss(mu, sigma)


def int_stream():
    i = 1
    while True:
        yield i
        i = i + 1