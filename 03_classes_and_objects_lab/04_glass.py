class Glass:
    capacity = 250

    def __init__(self):
        content = 0

    def fill(self, ml:int):
        if content + ml <= capacity:
            content += ml
            return f"Glass filled with {ml} ml"
        else:
            return f'Cannot add {ml} ml'

    def empty(self):
        content = 0
        return "Glass is now empty"

    def info(self):
        space_left = capacity - content
        return f'{space_left} ml left'

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
