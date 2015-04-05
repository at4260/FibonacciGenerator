def get_fibonacci(n):
    if type(n) is not int or n < 0:
        return None
    else:
        fib_list = [0,1]
        index = 2
        while index <= n:
            fib_list.append(fib_list[index - 1] + fib_list[index - 2])
            index += 1
        return fib_list[n]
