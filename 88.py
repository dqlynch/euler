import numpy as np


class FactorMemo:
    def __init__(self):
        self.memo = {}

    def get_factors(self, n):
        if n in self.memo:
            return self.memo.get(n)
        factors = get_factors(n)
        self.memo[n] = factors
        return factors

def get_factors(n):
    # Exclude 1 and n, n cannot be in its own product-sum
    factors = []
    for i in range(2, n):
        if n % i == 0:
            factors.append(i)
    factors.reverse()
    return factors

def _generate_products(n, memo, top=False):
    """Generate products without tails"""
    if not top:
        yield [n]
    factors = memo.get_factors(n)
    if not factors:
        return

    for divisor in factors:
        remainder = n // divisor

        for products in _generate_products(remainder, memo):
            yield [divisor] + products

def generate_products(n, k, memo):
    for products in _generate_products(n, memo, top=True):
        summation = sum(products)
        remainder = n - summation
        if remainder < k:
            #yield products + ([1] * remainder) # TODO can yield len(products) + remainder
            yield len(products) + remainder
        #while len(products) <= k:
        #    if summation == n:
        #        yield products
        #    if summation >= n:
        #        break
        #    summation += 1
        #    products += [1]

def solve(K):
    memo = FactorMemo()

    smallest = [None] * (K+1)
    i = 4
    while True:
        for k in generate_products(i, K, memo):
            #k = product
            if k <= K and smallest[k] is None:
                smallest[k] = i
        if None not in smallest[2:]:
            break
        i += 1
    #print(smallest)
    minimal_set = set(smallest[2:])
    print(minimal_set)
    print(sum(minimal_set))


if __name__=='__main__':
    solve(12000)
    #for products in generate_products(8, 8, memo):
    #    print(products)
