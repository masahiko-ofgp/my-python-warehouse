def fact_cps(n, cont):
    if n == 0:
        return cont(1)
    else:
        return fact_cc(n - 1, lambda x: cont(n * x))

def fact(n):
    return fact_cps(n, lambda x: x)

if __name__ == '__main__':
    """WARNING:
        Python has been setting recursionlimit 1000.
        If you want to change it, you need to do the following.

        import sys
        sys.setrecursionlimit(10000)

        However, setting too large numbers will crash.
    """
    print(fact(5))
