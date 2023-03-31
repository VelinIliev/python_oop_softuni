from functools import reduce


def even_parameters(function):
    def wrapper(*params):
        if all([isinstance(x, int) and x % 2 == 0 for x in params]):
            return function(*params)
        return f'Please use only even numbers!'

    return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))


@even_parameters
def multiply(*nums):
    return reduce(lambda x, y: x * y, nums)


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
