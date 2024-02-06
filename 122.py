def generate_sets(splits, i):
    if i == 1:
        yield {i, 1}
        return
    for s in splits[i]:
        yield s.union({i})


def solve(n):
    splits = [None] * (n+1)
    splits[1] = [{0}]

    for i in range(2, n+1):
        print(i)
        candidates = []
        for j in range(1, i // 2 + 1):
            j_r = i - j

            split_candidates = []
            for s in generate_sets(splits, j):
                for s_r in generate_sets(splits, j_r):
                    split_candidates.append(s.union(s_r))
                    candidates.append(s.union(s_r))

            min_s = min(split_candidates, key = lambda x: len(x))
            #candidates.append(min_s)

        min_len = len(min(candidates, key = lambda x: len(x)))
        splits[i] = []
        for c in candidates:
            if len(c) == min_len:
                splits[i].append(c)


    for i, split in enumerate(splits[1:]):
        print()
        print(i+1)
        for s in split:
            print(s)
            print(len(s))
    #print(len(splits[-1]))
    return splits

if __name__=='__main__':
    splits = solve(200)

    print()
    sum = 0
    for i, split in enumerate(splits[2:]):
        sum += len(min(split, key = lambda x: len(x)))
        print(i+1, len(split[0]))
    print()
    print(sum)
