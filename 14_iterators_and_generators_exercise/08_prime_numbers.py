def is_prime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def get_primes(numbers):
    for number in numbers:
        if number == 1:
            yield number
        else:
            if is_prime(number):
                yield number


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0, 101, 19, 21, 17])))