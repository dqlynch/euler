def solve(n):
    # Attempt brute force first, check from 1 to n-1 inclusive
    p = [1] # p[i] = p_i, ignore first index as duplicate for nicety
    for i in range(1, n):
        p.append((i * (3*i - 1)) // 2)
    p_ = set(p)

    for i in range(1, n-1):
        for j in range(i+1, n):
            if p[j] - p[i] < 0:
                break
            if p[i] + p[j] in p_:
                if p[j] - p[i] in p_:
                    print(i)
                    print(p[i])
                    print(p[j])
                    print(p[j] - p[i])



if __name__=='__main__':
    solve(10000)
