class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.i = count

    def __iter__(self):
        return self

    def __next__(self):
        while self.i > -1:
            current = self.i
            self.i -= 1
            return current
        raise StopIteration


iterator = countdown_iterator(20)
for item in iterator:
    print(item, end=" ")
