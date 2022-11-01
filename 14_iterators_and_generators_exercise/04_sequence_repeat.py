class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.i = 0
        self.end = number
        self.len = len(sequence) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.end - 1:
            index = self.i
            while index > self.len:
                index = index - (self.len + 1)
            current = self.sequence[index]
            self.i += 1
            return current
        else:
            raise StopIteration


result = sequence_repeat('abcdef', 8)
for item in result:
    print(item, end ='')
