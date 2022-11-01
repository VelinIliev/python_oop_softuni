def fibonacci():
    first_number = 0
    second_number = 0
    counter = 0
    while True:
        if counter == 0:
            first_number = counter
            yield counter
        elif counter == 1:
            second_number = counter
            yield counter
        else:
            new_number = first_number + second_number
            yield new_number
            first_number = second_number
            second_number = new_number
        counter += 1

generator = fibonacci()
for i in range(20):
    print(next(generator))
