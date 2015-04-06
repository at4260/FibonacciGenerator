def get_fibonacci(n):
    value_0 = 0
    value_1 = 1
    if n < 0:
        return "Not valid"
    elif n == 0:
        return value_0
    elif n == 1:
        return value_1
    else:
        while n >= 2:
            sum_of_values = value_0 + value_1
            value_0 = value_1
            value_1 = sum_of_values
            n = n - 1
        return sum_of_values
