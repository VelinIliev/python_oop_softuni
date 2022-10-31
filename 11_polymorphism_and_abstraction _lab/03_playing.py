class Guitar:
    def play(self):
        return "Playing the guitar"


def start_playing(x):
    return x.play()


guitar = Guitar()
print(start_playing(guitar))


class Children:
    def play(self):
        return "Children are playing"


children = Children()
print(start_playing(children))
