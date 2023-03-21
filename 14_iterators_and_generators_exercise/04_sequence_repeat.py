class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.index = -1
        self.end = number - 1
        self.len = len(self.sequence)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration

        self.index += 1
        return self.sequence[self.index % self.len]


result = sequence_repeat('abcdef', 40)
for item in result:
    print(item, end='')
