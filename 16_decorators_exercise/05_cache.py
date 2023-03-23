def cache(function):

    def wrapper(arg):
        if arg not in wrapper.log:
            wrapper.log[arg] = (function(arg))
        return wrapper.log[arg]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(50)
print(fibonacci.log)


