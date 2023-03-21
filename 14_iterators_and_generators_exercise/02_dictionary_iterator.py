class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.index = -1
        self.end = len(self.obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.end:
            raise StopIteration

        self.index += 1
        return list(self.obj.items())[self.index]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result1 = dictionary_iter({"name": "Peter", "age": 24})
for x in result1:
    print(x)
