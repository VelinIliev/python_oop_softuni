class dictionary_iter:
    def __init__(self, obj):
        self.obj = obj
        self.i = 0
        self.end = len(self.obj) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.i <= self.end:
            result = tuple
            for i, key in enumerate(self.obj.items()):
                if i == self.i:
                    result = key
            self.i += 1
            return result
        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result1 = dictionary_iter({"name": "Peter", "age": 24})
for x in result1:
    print(x)


