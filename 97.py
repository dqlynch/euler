import math

def gen_factors(n):
    """Brute force factors of n"""
    for i in range(1, n+1):
        if n % i == 0:
            yield i

if __name__=='__main__':
    # Find last 10 digits of 28433 x 2 ** 7830457 + 1
    exponent = 7830457
    acc = 28433

    # remove 32 from exponent
    while exponent > 32:
        exponent -= 32

        acc = (acc * (2**32 % 10**10)) % 10**10
    acc = (acc * (2**exponent % 10**10)) % 10**10
    print(acc + 1)
