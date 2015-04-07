def memoize(func):
    cached = {}
    def helper(n):
        if n not in cached:
            cached[n] = func(n)
            # print cached
        return cached[n]
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
