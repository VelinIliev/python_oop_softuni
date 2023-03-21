def logged(function):
    def wrapper(*args):
        return '\n'.join([f'you called {function.__name__}{args}', f'it returned {function(*args)}'])

    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
