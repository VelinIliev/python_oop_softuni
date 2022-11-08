def logged(function):
    def wrapper(*args):
        result = function(*args)
        return_string = ""
        return_string += f'you called {function.__name__}{args}\n'
        return_string += f'it returned {result}'
        return return_string
    return wrapper

# @logged
# def func(*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
