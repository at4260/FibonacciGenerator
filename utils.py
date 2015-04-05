def get_fibonacci(n):
    fib_list = []
    index = 0
    if type(n) is not int or n < 0:
        return None
    else:
        while index <= n:
            if index == 0:
                fib_list.append(0)
            elif index == 1:
                fib_list.append(1)
            else:
                fib_list.append(fib_list[index - 1] + fib_list[index - 2])
            index += 1
        return fib_list[n]
