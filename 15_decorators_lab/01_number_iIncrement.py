def number_increment(numbers):
    def increase():
        return list(map(lambda x: x + 1, numbers))

    return increase()


print(number_increment([1, 2, 3]))
