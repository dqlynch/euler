def fib_iter(n):
    if n == 1 or n == 2:
        return 1
    fn2 = 1
    fn1 = 1
    fn = None
    for i in range(n-2):
        fn = fn2 + fn1
        fn2 = fn1
        fn1 = fn
        if len(str(fn)) >= 1000:
            print(f"1000 digits found at index {i+3}, returning.")
            return fn
    return fn

if __name__ == '__main__':
    print(fib_iter(5000))
