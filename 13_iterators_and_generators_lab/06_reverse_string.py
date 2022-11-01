def reverse_text(string):
    yield string[::-1]


for char in reverse_text("step"):
    print(char, end='')
