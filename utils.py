def memoize(func):
    cached = {}
    def helper(x):
        if x not in cached:
            cached[x] = func(x)
            # print cached
        return cached[x]
    return helper

@memoize
def get_fibonacci(n):
    if n < 0:
        return "Not valid"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)
