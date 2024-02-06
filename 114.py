from time import perf_counter

def solve(n, m):
    """
    Return the number of blocks of at least k length that can be placed on a
    row of length n, with at least 1 space between each block.
    """
    # counts[i] is the  number of ways that it's possible to reach position i
    # where i is the start of a valid block. The final position is the number
    # of ways to fill the entire block.
    counts = [1] * (n+2)

    for i in range(n - (m-1)):
        for j in range(m, n - i + 1):
            # Place block of length j in position i. The next valid position
            # would then be i + j + 1.
            for k in range(i+j+1, n+2):
                counts[k] += counts[i]
        #print(counts)
    return counts[-1]


if __name__=='__main__':
    start = perf_counter()
    ans = solve(50, 3)
    stop = perf_counter()
    print(f"time: {(stop - start) * 1000}ms")
    print(ans)
