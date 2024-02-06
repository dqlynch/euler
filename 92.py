def next_c(c):
    next_c = 0
    while c:
        d = c % 10
        next_c += d*d
        c = c // 10
    #c_str = str(c)
    #next_c = 0
    #for d in c_str:
    #    next_c += int(d) * int(d)
    return next_c

def solve(n):
    """
    Find the number of digit chains that result in 89 (the rest end in 1).

    We know the max number is from 9,999,999 -> 81*7 = 567, so we can use a fixed
    size list such that list[i] is a bool representing whether the given number
    ends in 89. Thus we can precalculate this in O(k) time where k=567, and count
    n in (O(n)) time, resulting in O(n+k) = O(n) time.
    """

    ends_in_89 = [None] * (567 + 1)
    ends_in_89[1] = False
    ends_in_89[89] = True
    for i in range(1, 567 + 1):
        c = i
        while True:
            if ends_in_89[c] == True:
                ends_in_89[i] = True
                break
            if ends_in_89[c] == False:
                ends_in_89[i] = False
                break
            c = next_c(c)

    count = 0
    for i in range(1, n):
        c = next_c(i)
        if ends_in_89[c]:
            count += 1
    return count



if __name__=='__main__':
    print(solve(10000000))

    #c = 85
    #for i in range(10):
    #    print(c)
    #    c = next_c(c)


