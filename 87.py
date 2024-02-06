import math

def gen_primes(p):
    """
    Generate primes up to a maximum value p
    """
    sieve = [True] * p
    for i in range(2, p):
        if not sieve[i]:
            continue

        # Not a multiple of a previous number, mark its multiples False
        for j in range(i*2, p, i):
            sieve[j] = False

    for i in range(2, p):
        if sieve[i]:
            yield i


def solve(n):
    """n <= 50000000 for hardcoded bounds"""
    # bounds on each power
    primes_2 = [p**2 for p in gen_primes(7079 + 1)]
    primes_3 = [p**3 for p in gen_primes(373 + 1)]
    primes_4 = [p**4 for p in gen_primes(89 + 1)]


    # upper bound 1.6m calcs
    #print(len(primes_2) * len(primes_3) * len(primes_4))

    # Try simple count first
    unique = set()
    for p_4 in primes_4:
        if p_4 > n:
            break

        for p_3 in primes_3:
            partial_1 = p_4 + p_3
            if partial_1 > n:
                break

            for p_2 in primes_2:
                if partial_1 + p_2 >= n:
                    break
                #print(f"{p_2} + {p_3} + {p_4} = {partial_1 + p_2}")
                unique.add(partial_1 + p_2)
    return len(unique)


if __name__=='__main__':
    # need primes up to at least 7071
    # do we need the next prime greater? no it'll be over 50000000
    #print(math.sqrt(50000000))
    #print(50000000 ** (1. / 4))

    #print(solve(500))
    print(solve(50000000))
