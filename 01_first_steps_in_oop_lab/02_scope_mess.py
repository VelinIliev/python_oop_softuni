x = "global"


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print(f"inner: {x}")

    def change_global():
        global x
        x = "global: changed!"

    print(f'outer: {x}')
    inner()
    print(f"outer: {x}")
    change_global()


print(x)
outer()
print(x)