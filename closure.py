def closure():
    num = 0
    def inner_func():
        nonlocal num
        print(num)
        num = num + 1
    return inner_func


a = closure()
a()
a()


