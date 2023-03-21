def fibonacci():
    first_number = 0
    second_number = 1

    while True:
        yield first_number
        first_number, second_number = second_number, first_number + second_number


generator = fibonacci()
for i in range(5):
    print(next(generator))
