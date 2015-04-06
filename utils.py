def get_fibonacci(n):
    first_value = 0
    second_value = 1
    if n < 0:
        return "Not valid"
    elif n == 0:
        return first_value
    elif n == 1:
        return second_value
    else:
        while n >= 2:
            sum_of_values = first_value + second_value
            first_value = second_value
            second_value = sum_of_values
            n = n - 1
        return sum_of_values
