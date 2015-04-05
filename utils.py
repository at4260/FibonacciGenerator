def get_fibonacci(n):
    if n < 0:
        return "Not valid"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return get_fibonacci(n - 1) + get_fibonacci(n - 2)
