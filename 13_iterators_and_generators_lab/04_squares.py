def squares(end):
    start = 1
    while start <= end:
        yield start ** 2
        start += 1


print(list(squares(22)))
print(list(squares(2)))