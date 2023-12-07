from collections import deque


def test_merge(two):
    print()
    a, b = two[0], two[1]
    print(f"a: {a}, b: {b}")
    a, b = create_stack(a), create_stack(b)
    solution =  merge(a, b)
    print(f"after: {a}")
    print(f"bfter: {b}")
    str_sol = ""
    while solution:
        str_sol += solution.pop()
    print(f"solution: {str_sol}")


def merge(a, b):
    # TODO can truncate by length
    """a and b are stack of keylogs"""
    if not a:
        # a empty: copy b
        solution = deque()
        for i in range(len(b)):
            solution.append(b[i])
        return [solution]

    if not b:
        solution = deque()
        for i in range(len(a)):
            solution.append(a[i])
        return [solution]

    if a[-1] == b[-1]:
        # Match: pop both
        l = a.pop()
        b.pop()

        solutions = merge(a, b)
        for solution in solutions:
            solution.append(l)

        a.append(l)
        b.append(l)
        return solutions

    # Split and compare
    a_l = a.pop()
    a_solutions = merge(a, b)
    for a_solution in a_solutions:
        a_solution.append(a_l)
    a.append(a_l)

    b_l = b.pop()
    b_solutions = merge(a, b)
    for b_solution in b_solutions:
        b_solution.append(b_l)
    b.append(b_l)

    if len(a_solutions[0]) < len(b_solutions[0]):
        return a_solutions
    if len(b_solutions[0]) < len(a_solutions[0]):
        return b_solutions
    return a_solutions + b_solutions


def create_stack(a):
    # Construct stack from keylog. Item on top of stack (right of deque) is first in the keylog
    a_stack = deque()
    for i in range(len(a)):
        a_stack.append(a[len(a) - i - 1])
    return a_stack


def read_keylog(filename):
    with open(filename) as f:
        return [line.strip() for line in f]


def solve(keylog):
    keylog_stacks = [create_stack(log) for log in keylog]
    #keylog_stacks = keylog_stacks[:10]

    solutions = [keylog_stacks[0]]
    for i in range(1, len(keylog_stacks)):
        print(f"Num solutions: {len(solutions)}")
        for solution in solutions:
            print(strify(solution))

        new = []
        for solution in solutions:
            new += merge(solution, keylog_stacks[i])

        shortest_len = min(len(sol) for sol in new)
        solutions = []
        for sol in new:
            if len(sol) == shortest_len:
                solutions.append(sol)

    print(f"Num solutions: {len(solutions)}")
    for solution in solutions:
        print(strify(solution))

        # TODO trim longer ones

    # Check?
    for log in keylog_stacks:
        if not check(log, solutions[0]):
            print(f"FAILED: {log}")



def strify(solution):
    sol = solution.copy()
    str_sol = ""
    while sol:
        str_sol += sol.pop()
    return str_sol


def check(log, solution):
    log = log.copy()
    sol = solution.copy()
    l = None
    while log:
        l = log.pop()
        s = None
        while l != s:
            s = sol.pop()
            if not s:
                return False
    return True



if __name__ == '__main__':
    keylog = read_keylog("keylog.txt")

    base_case = ['', '680']
    same_case = ['123', '123']
    two_simple = ['319', '680']
    two_merge = ['680', '180']
    two_complex = ['310', '1680']

    #test_merge(base_case)
    #test_merge(same_case)
    #test_merge(two_simple)
    #test_merge(two_merge)
    #test_merge(two_complex)

    print(solve(keylog))
