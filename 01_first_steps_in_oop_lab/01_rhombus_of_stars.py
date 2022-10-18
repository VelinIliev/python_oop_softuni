n = int(input())

for x in range(n + 1):
    print(" " * (n - x) + "* " * x + " " * (n - x))
for y in range(n - 1, -1, -1):
    print(" " * (n - y) + "* " * y + " " * (n - y))