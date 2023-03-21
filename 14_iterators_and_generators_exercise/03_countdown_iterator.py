class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.number = count + 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):

        if self.number == self.end:
            raise StopIteration

        self.number -= 1
        return self.number


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
