def even(x):
    return x % 2 == 0

def odd(x):
    return x % 2 == 1

def positive(x):
    return x > 0

def negative(x):
    return x < 0

def prime(x):
    return False if 0 in [x % i for i in range(2, x//2 + 1)] or x < 2 else True